# Shutil is a Python module that provides a higher level interface for working with file and directories.

import shutil
'''
src → source file (original file)
dst → destination (where you want the copy)

shutil.copy(src, dst) - Copies a file from one location to another.

shutil.copy2(src, dst) - This is almost the same as copy() but preserves metadata.
Metadata includes things like: creation time, modification time, permissions

shutil.copytree(src, dst) - Used to copy an entire folder (directory).

shutil.move(src, dst) - Moves a file from one location to another (cut + paste).

shutil.rmtree(path) - Deletes an entire folder and everything inside it.

'''

