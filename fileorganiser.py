#fileorganiser

import os, shutil


path = input("Enter the directory path")
#target_path = r'/Users/HI20384787/Desktop/VScodeLearn/personalprojects/pr1/'
target_path = path.replace('\','/')

folder_name = ['html files','audio files', 'image files', 'text files']
for fd in folder_name:
    if not os.path.exists(target_path + fd):
        os.makedirs(target_path + fd)


for file in file_name:
    if '.html' in file and not os.path.exists(target_path + 'html files/' + file):
        shutil.move(target_path + file, target_path + 'html files/' + file)
    elif '.txt' in file and not os.path.exists(target_path + 'text files/' + file):
        shutil.move(target_path + file, target_path + 'text files/' + file)
    elif '.mp4' in file and not os.path.exists(target_path + 'audio files/' + file):
        shutil.move(target_path + file, target_path + 'audio files/' + file)
    elif '.jpeg' or '.jpg' in file and not os.path.exists(target_path + 'image files/' + file):
        shutil.move(target_path + file, target_path + 'image files/' + file)

