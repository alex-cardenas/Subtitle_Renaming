from pathlib import Path
import shutil
import os

def subtitles(path_str):
    os.chdir(path_str)
    path_file = os.getcwd()
    path = Path(path_file)
    print("working directory name is: ", path)
    print("file name should be: ", path.name)

    for file_path in path.iterdir():
        if file_path.name == "Subs":
            for sub_file in file_path.iterdir():
                print("subtitle file path is: ", sub_file)
                print("subtitle file name is: ", sub_file.name)
                shutil.copy2(sub_file, path)

if __name__ == "__main__":
    path_str = input("Enter path:\n")
    subtitles(path_str)

# print("old subtitle file name is: ", sub_file.name)
# sub_file.rename(path.name)
# print("new subtitle file name is: ", sub_file.name)
