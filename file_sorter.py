from pathlib import Path
import shutil

dir = input("Enter the path of the directory you want to sort:")

target_dir = Path(dir)

file_types = {
    ".pdf" : "PDF's",
    ".exe" : "Applications",
    ".zip" : "Zip_files",
    ".jpeg": "Images",
    ".png" : "Images",
    ".jpg" : "Images",
    ".xlsx": "Excel_Files",
    ".docx": "Word_Documents",
}


for file in target_dir.iterdir():
    file_ex = Path(file).suffix

    if file_ex in file_types:
        my_dir = Path(f"{dir}\{file_types[file_ex]}")
        my_dir.mkdir(exist_ok=True)

        shutil.move(file,f"{dir}\{file_types[file_ex]}")

        with open(rf"{dir}\Log.txt", "a") as f:
            f.write(f"{file} was moved to {dir}\{file_types[file_ex]} \n")