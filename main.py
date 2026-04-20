                                           # File Organizer
import os
import shutil
if not(os.path.exists("Images")) and (not(os.path.exists("images"))):
        os.mkdir("Images")
if not(os.path.exists("docs")) and not(os.path.exists("Docs")) and not(os.path.exists("Documents")) and not(os.path.exists("documents")):
        os.mkdir("Documents")
if not(os.path.exists("Videos")) and not(os.path.exists("videos")):
        os.mkdir("Videos")
current_folder = os.getcwd()


for root , dirs, files in os.walk("."):
    if "Images" in root:
        continue
    if "Documents" in root:
        continue
    if "Videos" in root:
        continue
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            full_path = os.path.join(root, file)
            destination = os.path.join(current_folder,"Images",file)
            print("Moving:",full_path,"->",destination)
            shutil.move(full_path, destination)
        elif file.endswith(".mp4") or file.endswith(".mkv"):
            full_path = os.path.join(root, file)
            destination = os.path.join(current_folder,"Videos",file)
            print("Moving:", full_path, "->", destination)
            shutil.move(full_path,destination)
        elif file.endswith(".docx") or file.endswith(".pdf") or file.endswith((".txt")):
            full_path = os.path.join(root, file)
            destination = os.path.join(current_folder,"Documents",file)
            print("Moving:", full_path, "->", destination)
            shutil.move(full_path,destination)











