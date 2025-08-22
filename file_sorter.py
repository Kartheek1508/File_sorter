from pathlib import Path
import shutil

dir = input("Enter the path of the directory you want to sort:")

preview = input("Do you want a preview? (y/n.)").lower() =="y"

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
preview_file = Path(rf"{dir}\Preview.txt")

for file in target_dir.iterdir():
    if file.is_file():
        file_ex = Path(file).suffix.lower()

        if file_ex in file_types:

            if preview:
                with open(preview_file, "a") as f:
                    f.write(f"Would move:{file} --> {dir}\{file_types[file_ex]} \n")
            
            else:
                folder_path = Path(f"{dir}\\{file_types[file_ex]}")
                folder_path.mkdir(exist_ok=True) 
                shutil.move(file, folder_path)  # Use the Path object consistently

if preview:
    print("Run again without dry-run to actually move files.")

    


            