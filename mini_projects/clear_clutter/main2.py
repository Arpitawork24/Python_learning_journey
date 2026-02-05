# a better code version

import os

test_folder = "mini_projects/clear_clutter/test_file"
jpg_folder = "mini_projects/clear_clutter/jpg_files"

# Create destination folder if not exists
if not os.path.exists(jpg_folder):
    os.mkdir(jpg_folder)

files = os.listdir(test_folder)

# Filter JPG files
jpg_files = []
for file in files:
    if file.endswith(".jpg"):
        jpg_files.append(file)

jpg_files.sort()

# ⭐ Find next available number (IMPORTANT PART)
existing_files = os.listdir(jpg_folder)

count = 1
while f"{count}.jpg" in existing_files:
    count += 1

# ⭐ Rename safely
for file in jpg_files:

    old_path = os.path.join(test_folder, file)

    new_name = f"{count}.jpg"
    new_path = os.path.join(jpg_folder, new_name)

    os.rename(old_path, new_path)

    count += 1
