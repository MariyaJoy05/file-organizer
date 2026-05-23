import os

folder = "test_folder"
files = os.listdir(folder)

print("Files found in floder:")
for file in files:
    print(file)
    