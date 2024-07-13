import os
import shutil

from image_loader import list_files_by_extension

def split_files_into_folders(file_list, files_per_folder, output_base_dir):
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    folder_index = 0
    for i in range(0, len(file_list), files_per_folder):
        folder_name = os.path.join(output_base_dir, f'folder_{folder_index}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for file in file_list[i:i + files_per_folder]:
            shutil.copy(file, folder_name)

        folder_index += 1



files_per_folder = 800  # Number of files per folder
output_base_dir = '/home/aoi/Documents/dataset/bridge/view_path'  # Base directory for the output folders

file_list = list_files_by_extension(directory="/home/aoi/Documents/dataset/bridge")
split_files_into_folders(file_list, files_per_folder, output_base_dir)
