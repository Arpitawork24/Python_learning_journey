import os
from pypdf import PdfWriter

folder = "mini_projects/merge_pdf/test_pdf"
output = "mini_projects/merge_pdf/merged2.pdf"

files = os.listdir(folder)
files.sort()

print("All files:", files)

merger = PdfWriter()
pdf_files = []

for file in files:
    if file.endswith(".pdf"):
        full_path = os.path.join(folder, file)
        pdf_files.append(full_path)

print("Filtered pdf files:")
print(pdf_files)

for pdf in pdf_files:
    print("Adding:", pdf)
    merger.append(pdf)

merger.write(output)
merger.close()

print("PDFs merged successfully!")