import os
import shutil
import datetime

# Folder to organize
folder = "test_folder"

# Log file
log_file = "organizer_log.txt"

def write_log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {message}\n"
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(log_entry.strip())

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

def organize_folder(folder):
    # Check if folder exists
    if not os.path.exists(folder):
        print(f"❌ Error: Folder '{folder}' not found!")
        return

    files = os.listdir(folder)

    # Check if folder is empty
    if not files:
        print("⚠️ Folder is empty - nothing to organize!")
        return

    write_log("--- Organizer Started ---")
    moved = 0

    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue

        try:
            name, extension = os.path.splitext(file)
            category = get_category(extension)
            category_path = os.path.join(folder, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            shutil.move(file_path, os.path.join(category_path, file))
            write_log(f"Moved {file} → {category}/")
            moved += 1

        except Exception as e:
            write_log(f"❌ Could not move {file} - Error: {e}")

    write_log(f"--- Organizer Finished | {moved} files organized ---")
    print(f"\n✅ Done! {moved} files organized.")

# Run the organizer
organize_folder(folder)