import os

files = os.listdir("mini_projects/clear_clutter/test_file")
print(files)

if (not os.path.exists("mini_projects/clear_clutter/jpg_files")):
    os.mkdir("mini_projects/clear_clutter/jpg_files")

# for file in files :
#     if file.endswith(".jpg"):
#         print(file)

jpg_files = []
for file in files :
    if file.endswith(".jpg"):
        jpg_files.append(file)
print("new")
print(jpg_files)

jpg_files.sort()
count = 1
for file in jpg_files:
    old_path = "mini_projects/clear_clutter/test_file/cat.jpg"
    new_path = "mini_projects/clear_clutter/jpg_files/1.jpg"
    os.rename(old_path, new_path)
    count += 1