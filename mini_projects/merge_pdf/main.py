import pypdf


from pypdf import PdfWriter
merger = PdfWriter()

print("Library working")

pdfs = ["mini_projects/merge_pdf/test_pdf/file1.pdf", "mini_projects/merge_pdf/test_pdf/file2.pdf", "mini_projects/merge_pdf/test_pdf/file3.pdf"]

for pdf in pdfs :
    merger.append(pdf)

merger.write("mini_projects/merge_pdf/merged.pdf")
merger.close()