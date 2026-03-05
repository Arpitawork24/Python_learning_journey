
import os
from pypdf import PdfWriter

files = os.listdir("mini_projects/merge_pdf/test_pdf")
print(files)

merger = PdfWriter()

merged2 = []
for file in files:
    if file.endswith(".pdf"):
        merged2.append(file)
        
print("Filtered pdf Files:")
print(merged2)

for pdf in merged2:
    merger.append(pdf)

merger.write("mini_projects/merge_pdf/merged2.pdf")
merger.close()