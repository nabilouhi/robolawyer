from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
import io
import sys
import os
import os.path
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import glob
import re
import shutil
from pathlib import Path
from .inputMethodforWM import *


class PrepareResult:

    def __init__(self, inputObj):
        self.inputObj = inputObj

    basedirPDF = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # userInputs = {
    #     'surname': 'Aman',
    #     'firstname': 'Kumar',
    #     'dateOfBirth': '19011992'
    # }

    def natural_key(self, string_):
        return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

    def createOrDeleteDirectory(self, directoryName):
        dirname = directoryName
        try:
            os.makedirs(dirname)
        except FileExistsError:
            shutil.rmtree(dirname)
            os.makedirs(dirname)

    def main(self):
        filename = 'applicationForm/dataPreparation/App_form.pdf'
        self.createOrDeleteDirectory('applicationForm/dataPreparation/pages')
        self.pdf_splitter(filename)

        paths = glob.glob(
            'applicationForm/dataPreparation/pages/App_form_page_*.pdf')
        output1 = self.create_watermark_pdf(self.inputObj[1], pos=1)
        output2 = self.create_watermark_pdf(self.inputObj[0], pos=2)
        self.createOrDeleteDirectory('applicationForm/dataPreparation/result')
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_1.pdf',
                       'applicationForm/dataPreparation/result/App_form_page_1.pdf', output1)
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_2.pdf',
                       'applicationForm/dataPreparation/result/App_form_page_2.pdf', output2)
    # ----
        paths.sort(key=self.natural_key)
        self.pdf_merger('pdf_merger2.pdf', paths)

    def pdf_splitter(self, path):
        fname = os.path.splitext(os.path.basename(path))[0]
        print("path", path)
        print(Path.cwd())
        pdf = PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
            output_filename = 'applicationForm/dataPreparation/pages/'+'{}_page_{}.pdf'.format(
                fname, page+1)
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
            print('Created: {}'.format(output_filename))

    def pdf_merger(self, output_path, input_paths):
        pdf_merger = PdfFileMerger()
        file_handles = []
        for path in input_paths:
            pdf_merger.append(path)
        with open(output_path, 'wb') as fileobj:
            pdf_merger.write(fileobj)

    def watermark(self, input_pdf, output_pdf, watermark_pdf):
        watermark = PdfFileReader(watermark_pdf)
        print(watermark_pdf)
        watermark_page = watermark.getPage(0)
        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)
        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

    def create_watermark_pdf(self, inputObj, pos):
        filename = 'applicationForm/dataPreparation/resultForm_' + \
            str(pos) + '.pdf'
        can = canvas.Canvas(filename, pagesize=letter)
        if pos == 1:
            can = firstPageInputs(self, can, inputObj)
        elif pos == 2:
            can = secondPageInputs(self, can, inputObj)
        else:
            print('bug reported')
        can.save()
        return filename


# if __name__ == "__main__":

#     main()
