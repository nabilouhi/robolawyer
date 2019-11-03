from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import io
import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


filename = 'App_form'
file_extension = 'pdf'

filled_out_file = filename + "-filled." + file_extension

surname = sys.argv[1]


def main():
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    can.drawString(30, 420, surname)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(
        filename + '.' + file_extension, strict=False)
    output = PdfFileWriter()

    totalPages = existing_pdf.numPages

    for page in range(totalPages):
        outputStream = io.FileIO(filled_out_file, 'wb')
        curPage = existing_pdf.getPage(page)
        curPage.mergePage(new_pdf.getPage(0))
        output.addPage(curPage)  # packet.seek(0)
        output.write(outputStream)
        outputStream.close()


if __name__ == "__main__":
    main()
