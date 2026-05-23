import os
import shutil
import datetime

# Folder to organize
folder = "test_folder"

log_file = "organizer_log.txt"

def write_log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f" {timestamp} {message}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)

    print(log_entry.strip())   
    

# Category rules
def get_category(extension):
    if extension in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"
    elif extension in [".pdf", ".docx", ".txt"]:
        return "Documents"
    elif extension in [".mp3", ".wav"]:
        return "Music"
    elif extension in [".mp4", ".mov"]:
        return "Videos"
    else:
        return "Others"

write_log("---Organizer Started---")


# Get all files
files = os.listdir(folder)

# Loop through each file
for file in files:
    # Build full path of the file
    file_path = os.path.join(folder, file)

    # Skip if it's a folder not a file
    if os.path.isdir(file_path):
        continue

    # Get extension and category
    name, extension = os.path.splitext(file)
    category = get_category(extension)

    # Create category folder if it doesn't exist
    category_path = os.path.join(folder, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Move the file
    shutil.move(file_path, os.path.join(category_path, file))
    write_log(f"Moved {file} → {category}/")

write_log("---Oraganizer Finished---")
print("\n Done! Check organizer_log.txt for details.")