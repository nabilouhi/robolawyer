from pathlib import Path
import requests
from tableaudocumentapi import Workbook
import os
import sys

filename = Path('metadata.pdf')
url = 'https://www.echr.coe.int/Documents/Application_Form_ENG.pdf'
response = requests.get(url)
filename.write_bytes(response.content)


sourceWB = Workbook(file_name)

sourceWB.save_as(os.path.join(os.path.dirname(filename)))


def file_save_as(self):
    fout = asksaveasfilename(defaultextension='.pdf')
    try:
        with open(fout, 'w') as output:
            for x in self.entries:
                output.write(x.get())
    except FileNotFoundError:
        print("Cancelled save or error in filename")


file_save_as()
# import sys
# import os
# import pathlib

# in_file = 'Application_Form.pdf'
# out_file = 'C:/Personal_DS/robo/robolawyer-project/home/static/pdf/App1.pdf'

# file1 = open(in_file, 'w')
# file1.write(out_file)
# file1.close()

# # from reportlab.pdfgen import canvas
# # from reportlab.lib import colors
# # from reportlab.lib.units import cm
# # from reportlab.lib.pagesizes import letter
# # import io
# # import sys
# # import os
# # import os.path
# # from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
# # import glob
# # import re
# # import shutil
# # from pathlib import Path

# # userInputs = {
# #     'surname': 'Aman',
# #     'firstname': 'Kumar',
# #     'dateOfBirth': '19011992'
# # }


# # def natural_key(string_):
# #     return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]


# # def createOrDeleteDirectory(directoryName):
# #     dirname = directoryName
# #     try:
# #         os.makedirs(dirname)
# #     except FileExistsError:
# #         shutil.rmtree(dirname)
# #         os.makedirs(dirname)


# # def main():
# #     filename = 'App_form.pdf'
# #     # dirname = 'pages'
# #     createOrDeleteDirectory('pages')
# #     pdf_splitter(filename)

# #     paths = glob.glob('pages/App_form_page_*.pdf')
# #     output = create_watermark_pdf(userInputs)
# #     createOrDeleteDirectory('result')
# #     watermark('pages/App_form_page_1.pdf',
# #               'result/App_form_page_1.pdf', output)
# # # ----
# #     paths.sort(key=natural_key)
# #     pdf_merger('pdf_merger2.pdf', paths)


# # def pdf_splitter(path):
# #     fname = os.path.splitext(os.path.basename(path))[0]
# #     print(fname)
# #     pdf = PdfFileReader(path)
# #     for page in range(pdf.getNumPages()):
# #         pdf_writer = PdfFileWriter()
# #         pdf_writer.addPage(pdf.getPage(page))
# #         output_filename = 'pages/'+'{}_page_{}.pdf'.format(
# #             fname, page+1)
# #         with open(output_filename, 'wb') as out:
# #             pdf_writer.write(out)
# #         print('Created: {}'.format(output_filename))


# # def pdf_merger(output_path, input_paths):
# #     pdf_merger = PdfFileMerger()
# #     file_handles = []
# #     for path in input_paths:
# #         pdf_merger.append(path)
# #     with open(output_path, 'wb') as fileobj:
# #         pdf_merger.write(fileobj)


# # def watermark(input_pdf, output_pdf, watermark_pdf):
# #     watermark = PdfFileReader(watermark_pdf)
# #     watermark_page = watermark.getPage(0)
# #     pdf = PdfFileReader(input_pdf)
# #     pdf_writer = PdfFileWriter()
# #     for page in range(pdf.getNumPages()):
# #         pdf_page = pdf.getPage(page)
# #         pdf_page.mergePage(watermark_page)
# #         pdf_writer.addPage(pdf_page)
# #     with open(output_pdf, 'wb') as fh:
# #         pdf_writer.write(fh)


# # def create_watermark_pdf(inputObj):
# #     filename = 'test_file.pdf'
# #     can = canvas.Canvas(filename, pagesize=letter)
# #     can.drawString(30, 420, inputObj["surname"])
# #     can.drawString(30, 380, inputObj["firstname"])
# #     baseX = 27
# #     for i in inputObj["dateOfBirth"]:
# #         baseY = 340
# #         can.drawString(baseX, baseY, i)
# #         baseX = baseX+17
# #     can.showPage()
# #     can.save()
# #     return filename

# #     # output = PdfFileWriter()
# # # filename = 'App_form'
# # # file_extension = 'pdf'

# # # filled_out_file = filename + "-filled." + file_extension

# # # # surname = 'sys.argv[1]'
# # # surname = 'aman'

# #     # def main():
# #     #     packet = io.BytesIO()
# #     #     can = canvas.Canvas(packet, pagesize=letter)

# #     #     can.drawString(30, 420, surname)
# #     #     can.save()

# #     #     packet.seek(0)
# #     #     new_pdf = PdfFileReader(packet)

# #     #     # existing_pdf = PdfFileReader(
# #     #     #     filename + '.' + file_extension, strict=False)
# #     #     existing_pdf = PdfFileReader(
# #     #         './App_form.pdf')
# #     #     output = PdfFileWriter()

# #     #     totalPages = existing_pdf.numPages

# #     #     for page in range(totalPages):
# #     #         outputStream = io.FileIO(filled_out_file, 'wb')
# #     #         curPage = existing_pdf.getPage(page)
# #     #         curPage.mergePage(new_pdf.getPage(0))
# #     #         output.addPage(curPage)  # packet.seek(0)
# #     #         output.write(outputStream)
# #     #         outputStream.close()


# # if __name__ == "__main__":

# #     main()
