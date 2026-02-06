import os

# Read all files from source folder
files = os.listdir("mini_projects/clear_clutter/test_file")
print(files)

# Create destination folder if it doesn't exist
if not os.path.exists("mini_projects/clear_clutter/jpg_files"):
    os.mkdir("mini_projects/clear_clutter/jpg_files")

# Filter only .jpg files
jpg_files = []
for file in files:
    if file.endswith(".jpg"):
        jpg_files.append(file)

print("Filtered JPG Files:")
print(jpg_files)

# Sort files for consistent numbering
jpg_files.sort()

# Get existing files to avoid overwriting
existing_files = os.listdir("mini_projects/clear_clutter/jpg_files")

# Find next available number (skip existing 1.jpg, 2.jpg, etc.)
count = 1
while str(count) + ".jpg" in existing_files:
    count += 1

# Rename and move files sequentially
for file in jpg_files:
    old_path = os.path.join("mini_projects/clear_clutter/test_file", file)

    new_name = str(count) + ".jpg"
    new_path = os.path.join("mini_projects/clear_clutter/jpg_files", new_name)

    os.rename(old_path, new_path)

    count += 1
