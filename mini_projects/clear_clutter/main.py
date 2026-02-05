import os

files = os.listdir("mini_projects/clear_clutter/test_file")
print(files)

if (not os.path.exists("mini_projects/clear_clutter/jpg_files")):
    os.mkdir("mini_projects/clear_clutter/jpg_files")

jpg_files = []
for file in files :
    if file.endswith(".jpg"):
        jpg_files.append(file)
print("new")
print(jpg_files)

jpg_files.sort()

# ⭐ NEW PART (added)
existing_files = os.listdir("mini_projects/clear_clutter/jpg_files")

count = 1
while str(count) + ".jpg" in existing_files:
    count += 1
# ⭐ END NEW PART

for file in jpg_files:
    old_path = os.path.join("mini_projects/clear_clutter/test_file", file)

    new_name = str(count) + ".jpg"
    new_path = os.path.join("mini_projects/clear_clutter/jpg_files", new_name)

    os.rename(old_path, new_path)

    count += 1
