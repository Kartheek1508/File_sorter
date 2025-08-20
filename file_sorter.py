from pathlib import Path
import shutil

dir = input("Enter the path of the directory you want to sort:")

target_dir = Path(dir)

file_types = {
    ".pdf" : "PDF's",
    ".exe" : "Applications",
    ".zip" : "Zip_files",
    ".jpeg": "Images",
    ".png" : "Images"
}


for file in target_dir.iterdir():
    file_ex = Path(file).suffix

    if file_ex in file_types:
        my_dir = Path(f"{dir}\{file_types[file_ex]}")
        my_dir.mkdir(exist_ok=True)

        shutil.move(file,f"{dir}\{file_types[file_ex]}")

