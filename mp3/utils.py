import PySimpleGUI as sg
import os


directories = []


def get_files_inside_directory_not_recursive(directory):
    global directories
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)
    print(directories)
    return directories


directory = sg.popup_get_folder('Select Music Directory')
directories = get_files_inside_directory_not_recursive(directory)
