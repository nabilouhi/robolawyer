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
import logging

logger = logging.getLogger(__name__)


class PrepareResult:

    def __init__(self, inputObj, sessionID, spclReplies):
        self.inputObj = inputObj
        self.sessionID = sessionID
        self.spclReplies = spclReplies

    basedirPDF = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def natural_key(self, string_):
        return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

    def createOrDeleteDirectory(self, directoryName):
        dirname = directoryName
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        else:
            shutil.rmtree(dirname)
            os.makedirs(dirname)

    def main(self):
        """ next 3 lines to be executed when there is a change in application form file. Looks for the 
         formatting changes if needed."""
        # filename = 'applicationForm/dataPreparation/App_form.pdf'
        # self.createOrDeleteDirectory('applicationForm/dataPreparation/pages')
        # self.pdf_splitter(filename)
        sof = self.inputObj['page4']['page4[stOfFacts]']
        sof1 = sof[:3890]
        sof2 = sof[3790:8140]
        sof3 = sof[8140: 12500]

        
        article = []
        article.append(self.spclReplies[1])
        article.append(self.spclReplies[2])

        complains = []
        complains.append(self.spclReplies[3])
        complains.append([m+' '+ str(n) for m,n in zip(self.spclReplies[5], self.spclReplies[4])])

        docs = []
        docs.append(self.spclReplies[6])
        docs.append(self.spclReplies[7])
        docs.append(self.spclReplies[8])
        docs.append(self.spclReplies[9])

        paths = glob.glob(
            'applicationForm/dataPreparation/pages/App_form_page_*.pdf')
        
        codeList = []
        barCodeText = "ENG - 2018/1|"
        for key, value in self.inputObj['page2'].items():
            if key not in ["page2[applicantType]", "page2[applicantAnon]", "page2[applicantAnonExp]", "page2[indAddress]", "page2[orgAddress]"]:
                barCodeText+= value+"|"

        for key, value in self.inputObj['page3'].items():
            if key not in ["page3[indRepresentativeType]","page3[indNLCapacity]", "page3[orgnlCapacity]", "page3[orgnlAddress]", "page3[orglAddress]", "page3[indNLAddress]", "page3[indLAddress]"]:
                barCodeText+= value+"|"
        codeList.append(barCodeText)
        codeList.append(self.sessionID)

        self.createOrDeleteDirectory('applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/')
        self.createOrDeleteDirectory('applicationForm/dataPreparation/results/'+self.sessionID+'/watermark/')
        output1 = self.create_watermark_pdf(self.inputObj['page2'], pos=1)
        output2 = self.create_watermark_pdf(self.spclReplies[0], pos=2)
        if self.inputObj['page2']["page2[applicantType]"] == "Individual":
            output3 = self.create_watermark_pdf(self.inputObj['page3'], pos=3)
            output4 = self.create_watermark_pdf([], pos=4)
        else:
            output3 = self.create_watermark_pdf([], pos=3)
            output4 = self.create_watermark_pdf(self.inputObj['page3'], pos=4)
        output5 = self.create_watermark_pdf(sof1, pos=5)
        output6 = self.create_watermark_pdf(sof2, pos=6)
        output7 = self.create_watermark_pdf(sof3, pos=7)
        output8 = self.create_watermark_pdf(article, pos=8)
        output9 = self.create_watermark_pdf(article, pos=9)
        output10 = self.create_watermark_pdf(complains, pos=10)
        output11 = self.create_watermark_pdf(self.inputObj['page6'], pos=11, tempInput=self.inputObj['page7'])
        output12 = self.create_watermark_pdf(docs, pos=12)
        output13 = self.create_watermark_pdf(self.inputObj['page9'], pos=13, tempInput=codeList)
        

        self.create_New_Pdf(docs)
        # print(self.inputObj)
        anonValue = self.inputObj['page2']['page2[applicantAnonExp]']
        anonValue = anonValue.replace(" ", "")
        if anonValue != '':
            filenameAnon = 'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_14.pdf'
            go(filenameAnon, self.inputObj['page2']['page2[applicantAnonExp]'], anonymityPage)

        sofValue = self.inputObj['page4']['page4[stOfFactsExtra]']
        sofValue = sofValue.replace(" ", "")
        if sofValue != '':
            filenameStOfFacts = 'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_15.pdf'
            go(filenameStOfFacts, self.inputObj['page4']['page4[stOfFactsExtra]'], extraStOfFactsFirstPage, extraStOfFactsLaterPage)

        logger.warning("Your log message is here")

        
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_1.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_1.pdf', output1)
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_2.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_2.pdf', output2),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_3.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_3.pdf', output3),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_4.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_4.pdf', output4),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_5.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_5.pdf', output5),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_6.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_6.pdf', output6),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_7.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_7.pdf', output7),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_8.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_8.pdf', output8),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_9.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_9.pdf', output9),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_10.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_10.pdf', output10),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_11.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_11.pdf', output11),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_12.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_12.pdf', output12),
        self.watermark('applicationForm/dataPreparation/pages/App_form_page_13.pdf',
                       'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_13.pdf', output13),

        resultPath = glob.glob('applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_*.pdf')
        resultPath.sort(key=self.natural_key)
        self.pdf_merger('applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/finalForm.pdf', resultPath)

    def pdf_splitter(self, path):
        fname = os.path.splitext(os.path.basename(path))[0]
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
        watermark_page = watermark.getPage(0)
        pdf = PdfFileReader(input_pdf)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.getNumPages()):
            pdf_page = pdf.getPage(page)
            pdf_page.mergePage(watermark_page)
            pdf_writer.addPage(pdf_page)
        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)
        fh.close()

    def create_watermark_pdf(self, inputObj, pos, tempInput=None):
        filename = 'applicationForm/dataPreparation/results/'+self.sessionID+'/watermark/resultForm_' + \
            str(pos) + '.pdf'
        can = canvas.Canvas(filename, pagesize=letter)
        if pos == 1:
            can = firstPageInputs(self, can, inputObj)
        elif pos == 2:
            can = secondPageInputs(self, can, inputObj)
        elif pos == 3:
            can = thirdPageInputs(self, can, inputObj)
        elif pos == 4:
            can = fourthPageInputs(self, can, inputObj)
        elif pos == 5:
            can = fifthPageInputs(self, can, inputObj)
        elif pos == 6:
            can = sixthPageInputs(self, can, inputObj)
        elif pos == 7:
            can = seventhPageInputs(self, can, inputObj)
        elif pos == 8:
            can = eighthPageInputs(self, can, inputObj)
        elif pos == 9:
            can = ninthPageInputs(self, can, inputObj)
        elif pos == 10:
            can = tenthPageInputs(self, can, inputObj)
        elif pos == 11:
            can = eleventhPageInputs(self, can, inputObj, tempInput)
        elif pos == 12:
            can = twelvthPageInputs(self, can, inputObj)
        elif pos==13:
            can = thirteenthPageInputs(self, can, inputObj, tempInput)
        else:
            print('bug reported')
        can.save()
        return filename

    def create_New_Pdf(self, inputObj):
        totalBookmark = len(inputObj[1])
        if inputObj[1] == ['']:
            print("no doc entered")
        else: 
            docs4List = sortDocumentsDate(self, inputObj)
            for single in range(totalBookmark):
                filename = 'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_' + \
                    str(15+single) + '.pdf'
                can = canvas.Canvas(filename, pagesize=letter)
                can = bookmarkPageInputs(self, can, [docs4List[1][single], docs4List[4][single]])
                can.save()

    def createAnonymityDoc(self, inputObj):
        if inputObj == '':
            print('no anonymity request')
        else:
            filename = 'applicationForm/dataPreparation/results/'+self.sessionID+'/finalPage/Result_form_page_' + \
                    str(14) + '.pdf'
            can = canvas.Canvas(filename, pagesize=letter)
            can = anonymityDoc(self, can, inputObj)
            can.save()


def anonymityPage(canvas, doc):
    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]
    pageinfo = "Request of Anonymity"
    Title = "Request of Anonymity"
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"Page %s" % pageinfo)
    canvas.restoreState()

def anonymityLaterPages(canvas, doc):
    pageinfo = "Request of Anonymity"
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def extraStOfFactsFirstPage(canvas, doc):
    PAGE_HEIGHT=defaultPageSize[1]
    PAGE_WIDTH=defaultPageSize[0]
    pageinfo = "Statement of Facts(Extra)"
    Title = "Statement of Facts"
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch," %s" % pageinfo)
    canvas.restoreState()

def extraStOfFactsLaterPage(canvas, doc):
    pageinfo = "Statement of Facts (Extra)"
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()