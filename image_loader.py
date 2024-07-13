import os
import re

from PIL import Image
from multiprocessing import Pool

import config


def thumbnails(image_fns, size=(30, 30), number_of_cores_to_use=config.THREAD_LOAD_DATA):
    def thumbnail(image_detail):
        """
        get image thumbnail with given size
        """
        size = (30, 30)
        image_fn, size  = image_detail
        try:
            im = Image.open(image_fn)
            im.thumbnail(size)
        except Exception as e:
            return e
        return True

    pool = Pool(number_of_cores_to_use)
    results = pool.map(thumbnail, zip(image_fns, [size] * len(image_fns)))
    return results


def list_files_by_extension(directory, extensions=['.jpeg', '.png', '.jpg'], regex_pattern=None):
    """
    Lists all files in the given directory with the specified extensions.

    :param directory: The directory to search in.
    :param extensions: A list of file extensions to look for.
    :return: A list of file paths that match the extensions.
    """
    matching_files = []
    pattern = None
    if regex_pattern is not None:
        pattern = re.compile(regex_pattern)

    # Ensure extensions are in lower case for case insensitive matching
    extensions = [ext.lower() for ext in extensions]

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                if (pattern is None) or (pattern is not None and pattern.search(file)):
                    matching_files.append(os.path.join(root, file))

    return matching_files


# if __name__ == '__main__':
#     directory = '.'
#     extensions = ['.jpeg', '.png', '.jpg']
#     files = list_files_by_extension(directory, extensions)

#     # Print the list of matching files
#     for file in files:
#         print(file)
