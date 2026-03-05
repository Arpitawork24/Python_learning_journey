"""
PDF Merger

This script merges all PDF files from a folder into a single PDF.
Files are merged in alphabetical order.
"""

import os
from pypdf import PdfWriter

# Folder containing input PDFs
folder = "mini_projects/merge_pdf/test_pdf"

# Output merged PDF file
output = "mini_projects/merge_pdf/merged2.pdf"

files = os.listdir(folder)
files.sort()  # ensure predictable merge order

print("All files:", files)

merger = PdfWriter()
pdf_files = []

# Collect only PDF files
for file in files:
    if file.endswith(".pdf"):
        full_path = os.path.join(folder, file)
        pdf_files.append(full_path)

print("Filtered pdf files:")
print(pdf_files)

# Add each PDF to the merger
for pdf in pdf_files:
    print("Adding:", pdf)
    merger.append(pdf)

# Write merged output
merger.write(output)
merger.close()

print("PDFs merged successfully!")