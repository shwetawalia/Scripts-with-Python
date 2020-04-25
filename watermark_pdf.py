import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader


pdfRead = PyPDF2.PdfFileReader('/home/learning/Downloads/sample.pdf')
watermark_page = pdfRead.getPage(0)

pdf_reader = PdfFileReader('/home/learning/Desktop/watermark.pdf')
pdf_writer = PdfFileWriter()


for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

with open('marked.pdf', 'wb') as out:

    pdf_writer.write(out)




