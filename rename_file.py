# secret message - mini project
import os


def rename_files():
    # 1. get file names from a folder
    # r means raw path
    # change the part after r to the path where the extracted folder is
    filename_list = os.listdir(r"C:\Users\user\Desktop\SecretMessage")
    print(filename_list)

    path = os.getcwd()
    os.chdir(r"C:\Users\user\Desktop\SecretMessage")

    # 2. for each file, rename filename ie remove numbers from it
    for file_name in filename_list:
        os.rename(file_name, file_name.translate(str.maketrans("", "", "0123456789")))
    os.chdir(path)
rename_files()