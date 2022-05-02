from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1 = PdfFileReader("file1.pdf")
pdf_file2 = PdfFileReader("file2.pdf")
pdf_file3 = PdfFileReader("file3.pdf")
pdfoutput = PdfFileMerger()
pdfoutput.append(pdf_file1)
pdfoutput.append(pdf_file2)
pdfoutput.append(pdf_file3)

with open("mergedfile.pdf", "wb") as finaloutput:
    pdfoutput.write(finaloutput)