import os

folder = "test_folder"
files = os.listdir(folder)

print("Files found in floder:")
for file in files:
    print(file)

print("\nFiles with their types:")
for file in files:
    name,extension = os.path.splitext(file)
    print(file,"->",extension)    

print("\nCategory of each file:")
for file in files:
    name,extension = os.path.splitext(file)

    if extension in [".jpg" , ".jpeg" , ".png" , ".gif"]:
        category = "Images"
    elif extension in [".pdf",".docx",".txt"]:
        category = "Documents"
    elif extension in [".mp3",".wav"]:
        category = "Music"
    elif extension in [".mp4" , ".mov"]:
        category = "Videos"
    else:
        category = "Others"

    print(file,"->",category)     

