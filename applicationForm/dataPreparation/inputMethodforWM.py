from textwrap import wrap
from reportlab.graphics import shapes
from .countryCoordDict import coordinateDict

customFont = 'Courier'
customFontSize = 11

def firstPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont(customFont, customFontSize)
    can.setFont(customFont, customFontSize)
    if inputObj["page2[applicantType]"] == "Individual":
        can.drawString(25, 420, inputObj["page2[indSurname]"])
        can.drawString(25, 380, inputObj["page2[indFirstName]"])
        baseX = 27
        birthdate = inputObj["page2[birthDate]"]
        for i in birthdate.replace('/', ''):
            baseY = 340
            can.drawString(baseX, baseY, i)
            baseX = baseX+17

        indPobNew = modifyCountryNames(inputObj["page2[indPob]"])
        can.drawString(25, 285, indPobNew)
        indNationalityNew = modifyCountryNames(inputObj["page2[indNationality]"])
        can.drawString(25, 245, indNationalityNew)

        addressOne = inputObj["page2[indAddress]"]
        addressOneLength = len(addressOne)
        newAddress = "\n".join(wrap(addressOne, 40))
        t.setTextOrigin(25, 208)
        t.textLines(newAddress)
        can.drawText(t)

        can.drawString(25, 110, inputObj["page2[indPhone]"])
        can.drawString(25, 70, inputObj["page2[indEmail]"])

        if "page2[applicantSex]" in inputObj:
            if  inputObj["page2[applicantSex]"] == 'Male':
                can.circle(78,46, 4, fill=1)
            elif inputObj["page2[applicantSex]"] == 'Female':
                can.circle(148, 46, 4, fill=1)
        else:
            print("no value entered")

        

    else:
        can.drawString(25, 285, "")
        can.drawString(25, 245, "")
        nameOne = inputObj["page2[orgName]"]
        newNameOne = "\n".join(wrap(nameOne, 40))
        t.setTextOrigin(308, 422)
        t.textLines(newNameOne)
        can.drawText(t)

        can.drawString(310, 360, inputObj["page2[orgID]"])

        baseX = 310
        incorpDate = inputObj["page2[orgDate]"]
        for i in incorpDate.replace('/', ''):
            baseY = 320
            can.drawString(baseX, baseY, i)
            baseX = baseX+17
        
        can.drawString(310, 265, inputObj["page2[orgActivity]"])
        
        addressTwo = inputObj["page2[orgAddress]"]
        newAddressTwo = "\n".join(wrap(addressTwo, 40))
        t.setTextOrigin(310, 227)
        t.textLines(newAddressTwo)

        can.drawString(310, 88, inputObj["page2[orgPhone]"])
        can.drawString(310, 48, inputObj["page2[orgEmail]"])
        can.drawText(t)
        
    can.showPage()
    return can


def secondPageInputs(self, can, inputObj):
    selectedStates = inputObj
    for selectedOne in selectedStates:
        if selectedOne in coordinateDict:
            can.drawString(coordinateDict[selectedOne]['x'], coordinateDict[selectedOne]['y'], 'X')
    can.showPage()
    return can

def thirdPageInputs(self, can, inputObj):
    can.setFont(customFont, customFontSize)
    if inputObj == []:
        blankPageInputs(self, can)
    else: 
        t = can.beginText()
        t.setFont(customFont, customFontSize)
        if inputObj["page3[indRepresentativeType]"] == "non-lawyer":
            can.drawString(25, 662, inputObj["page3[indNLCapacity]"])
            can.drawString(25, 622, inputObj["page3[indNLSurname]"])
            can.drawString(25, 581, inputObj["page3[indNLFirstName]"])

            indNLNationalityNew = modifyCountryNames(inputObj["page3[indNLNationality]"])
            can.drawString(25, 544, indNLNationalityNew)
            addressThree = inputObj["page3[indNLAddress]"]
            addressThreeLength = len(addressThree)
            newAddress = "\n".join(wrap(addressThree, 40))
            t.setTextOrigin(25, 503)
            t.textLines(newAddress)
            can.drawText(t)
            can.drawString(25, 402, inputObj["page3[indNLTel]"])
            can.drawString(25, 322, inputObj["page3[indNLFax]"])
            can.drawString(25, 362, inputObj["page3[indNLEmail]"])

        elif inputObj["page3[indRepresentativeType]"] == "lawyer":
            can.drawString(310, 662, inputObj["page3[indLSurname]"])
            can.drawString(310, 622, inputObj["page3[indLFirstName]"])

            indLNationalityNew = modifyCountryNames(inputObj["page3[indLNationality]"])
            can.drawString(310, 581, indLNationalityNew)
            addressFour = inputObj["page3[indLAddress]"]
            newAddressFour = "\n".join(wrap(addressFour, 40))
            t.setTextOrigin(310, 543)
            t.textLines(newAddressFour)
            can.drawText(t)
            can.drawString(310, 402, inputObj["page3[indLTel]"])
            can.drawString(310, 322, inputObj["page3[indLFax]"])
            can.drawString(310, 362, inputObj["page3[indLEmail]"])
            can.drawString(30, 37, inputObj["page3[indIndeComms]"])
        
        else:
            print("nothing printed here for self representing individual")

    can.showPage()

    return can

def fourthPageInputs(self, can, inputObj):
    can.setFont(customFont, customFontSize)
    if inputObj == []:
        blankPageInputs(self, can)
    else:
        t = can.beginText()
        t.setFont(customFont, customFontSize)
        if inputObj["page3[orgRepresentativeType]"] == "orgNoLawyer":
            can.drawString(25, 666, inputObj["page3[orgnlCapacity]"])
            can.drawString(25, 626, inputObj["page3[orgnlSurname]"])
            can.drawString(25, 585, inputObj["page3[orgnlFirstName]"])

            orgnlNationalityNew = modifyCountryNames(inputObj["page3[orgnlNationality]"])
            can.drawString(25, 548, orgnlNationalityNew)
            addressFour = inputObj["page3[orgnlAddress]"]
            newAddressFour = "\n".join(wrap(addressFour, 40))
            t.setTextOrigin(25, 508)
            t.textLines(newAddressFour)
            can.drawText(t)
            
            can.drawString(25, 367, inputObj["page3[orgnlTel]"])
            can.drawString(25, 327, inputObj["page3[orgnlFax]"])
            can.drawString(25, 407, inputObj["page3[orgnlEmail]"])

        elif inputObj["page3[orgRepresentativeType]"] == "orgYesLawyer":
            can.drawString(310, 666, inputObj["page3[orglSurname]"])
            can.drawString(310, 626, inputObj["page3[orglFirstName]"])

            orglNationalityNew = modifyCountryNames(inputObj["page3[orglNationality]"])
            can.drawString(310, 585, orglNationalityNew)
            addressFive = inputObj["page3[orglAddress]"]
            newAddressFive = "\n".join(wrap(addressFive, 40))
            t.setTextOrigin(310, 548)
            t.textLines(newAddressFive)
            can.drawText(t)
            can.drawString(310, 367, inputObj["page3[orglTel]"])
            can.drawString(310, 327, inputObj["page3[orglFax]"])
            can.drawString(310, 407, inputObj["page3[orglEmail]"])
            can.drawString(25, 37, inputObj["page3[orgIndeComms]"])
    
        else:
            can.drawString(25, 37, inputObj["page3[indIndeCommsSelf]"])

    can.showPage()
    return can


def fifthPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont(customFont, customFontSize)
    stOfFactsText = inputObj
    stOfFactsText = stOfFactsText.replace('\r\n','\n')
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 82))
    newStOfFactsList = newStOfFactsText.split('\n')
    t.setTextOrigin(25, 670)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def sixthPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont(customFont, customFontSize)
    stOfFactsText = inputObj
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 82))
    t.setTextOrigin(25, 760)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def seventhPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont(customFont, customFontSize)
    stOfFactsText = inputObj
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 82))
    t.setTextOrigin(25, 760)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def eighthPageInputs(self, can, inputObj):
    yCoord = 750
    for item in range(len(inputObj[0])):
        if item>1:
            break
        t1 = can.beginText()
        t1.setFont(customFont, customFontSize)
        if len(inputObj[0]) > 1:
            article = inputObj[0][item]
            articleExp = inputObj[1][item]
        elif len(inputObj[0]) == 1:
            article = inputObj[0][0]
            articleExp = inputObj[1][0]
        else:
            print("error reported in EighthPageInputs")

        newArticle = "\n".join(wrap(article, 20))
        t1.setTextOrigin(25, yCoord)
        t1.textLines(newArticle)
        can.drawText(t1)

        t2 = can.beginText()
        t2.setFont(customFont, customFontSize)
        newArticleExp = "\n".join(wrap(articleExp, 59))
        t2.setTextOrigin(180, yCoord)
        t2.textLines(newArticleExp)
        can.drawText(t2)
        yCoord -= nextLineForPara(len(newArticleExp), 59, 13.7)

    can.showPage()
    return can

def ninthPageInputs(self, can, inputObj):
    yCoord = 750
    for item in range(len(inputObj[0])):
        if item>1:
            t1 = can.beginText()
            t1.setFont(customFont, customFontSize)
            if len(inputObj[0]) > 1:
                article = inputObj[0][item]
                articleExp = inputObj[1][item]
            elif len(inputObj[0]) == 1:
                article = inputObj[0][0]
                articleExp = inputObj[1][0]
            else:
                print("error reported in EighthPageInputs")

            newArticle = "\n".join(wrap(article, 20))
            t1.setTextOrigin(25, yCoord)
            t1.textLines(newArticle)
            can.drawText(t1)

            t2 = can.beginText()
            t2.setFont(customFont, customFontSize)
            newArticleExp = "\n".join(wrap(articleExp, 59))
            t2.setTextOrigin(180, yCoord)
            t2.textLines(newArticleExp)
            can.drawText(t2)
            yCoord -= nextLineForPara(len(newArticleExp), 59, 13.7)


    can.showPage()
    return can

def tenthPageInputs(self, can, inputObj):
    yCoord = 705
    for item in range(len(inputObj[0])):
        t1 = can.beginText()
        t1.setFont(customFont, customFontSize)
        if len(inputObj[0]) > 1:
            complain = inputObj[0][item]
            remedies = inputObj[1][item]
        elif len(inputObj[0]) == 1:
            complain = inputObj[0][0]
            remedies = inputObj[1][0]
        else:
            print("error reported in TenthPageInputs")

        newComplain = "\n".join(wrap(complain, 22))
        t1.setTextOrigin(25, yCoord)
        t1.textLines(newComplain)
        can.drawText(t1)


        t2 = can.beginText()
        t2.setFont(customFont, customFontSize)
        newRemedy = "\n".join(wrap(remedies, 58))
        t2.setTextOrigin(185, yCoord)
        t2.textLines(newRemedy)
        can.drawText(t2)
        yCoord -= nextLineForPara(len(newRemedy), 60, 14.5)

    can.showPage()
    return can

def eleventhPageInputs(self, can, inputObj, secondInput):
    if "page6[appealAvailable]" in inputObj:
            if  inputObj["page6[appealAvailable]"] == 'Yes':
                can.circle(466,787, 4, fill=1)
                t = can.beginText()
                t.setFont(customFont, customFontSize)
                appealDescribe = inputObj['page6[appealDescribe]']
                newAppealDescribe = "\n".join(wrap(appealDescribe, 82))
                t.setTextOrigin(25, 735)
                t.textLines(newAppealDescribe)
                can.drawText(t)
            elif inputObj["page6[appealAvailable]"] == 'No':
                can.circle(466, 768, 4, fill=1)
            else:
                print("no value entered")

    if "page7[intInvestigation]" in secondInput:
            if secondInput["page7[intInvestigation]"] == 'Yes':
                can.circle(466, 475, 4, fill=1)
                t = can.beginText()
                t.setFont(customFont, customFontSize)
                intInvestigationDesc = secondInput['page7[intInvestigationDesc]']
                newIntInvestigationDesc = "\n".join(wrap(intInvestigationDesc, 82))
                t.setTextOrigin(25, 390)
                t.textLines(newIntInvestigationDesc)
                can.drawText(t)
            elif secondInput["page7[intInvestigation]"] == 'No':
                can.circle(466.2, 456.5, 4, fill=1)
            else:
                print("no value entered")
    
    if "page7[prevApplications]" in secondInput:
            if secondInput["page7[prevApplications]"] == 'Yes':
                can.circle(466, 129, 4, fill=1)
                t = can.beginText()
                t.setFont(customFont, customFontSize)
                prevAppDesc = secondInput['page7[prevAppDesc]']
                newPrevAppDesc = "\n".join(wrap(prevAppDesc, 82))
                t.setTextOrigin(25, 75)
                t.textLines(newPrevAppDesc)
                can.drawText(t)
            elif secondInput["page7[prevApplications]"] == 'No':
                can.circle(466.2, 110, 4, fill=1)
            else:
                print("no value entered")
    
    can.showPage()
    return can

def twelvthPageInputs(self, can, inputObj):
    if inputObj[0] == ['']:
        print("no value entered twelvth")
    else:
        [dateListNew, descListNew, pageListNew, pageListTemp] = sortDocumentsDate(self, inputObj)
        pageListNew = add_one_by_one(pageListTemp)
        yCoord = 655
        for item in range(len(inputObj[0])):
            t1 = can.beginText()
            t1.setFont(customFont, customFontSize)
            if len(inputObj[0]) > 1:
                desc = descListNew[item]
                page = pageListNew[item]
            elif len(inputObj[0]) == 1:
                desc = descListNew[0]
                page = pageListNew[0]
            else:
                print("error reported in TwelvethPageInputs")

            newDesc = "\n".join(wrap(desc, 10))
            t1.setTextOrigin(40, yCoord)
            t1.textLines(newDesc)
            can.drawText(t1)

            t2 = can.beginText()
            t2.setFont(customFont, customFontSize)
            newPage = "\n".join(wrap(page, 5))
            t2.setTextOrigin(550, yCoord)
            t2.textLines(newPage)
            can.drawText(t2)
            yCoord -= nextLineForPage12(len(desc), 70, 8.5)

    can.showPage()
    return can


def thirteenthPageInputs(self, can, inputObj, tempInput):
    import io
    from reportlab.lib.utils import Image, ImageReader
    import os
    from django.conf import settings
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM

    t = can.beginText()
    t.setFont(customFont, customFontSize)
    comments = inputObj['page9[formComments]']
    newComments = "\n".join(wrap(comments, 82))
    t.setTextOrigin(25, 730)
    t.textLines(newComments)
    can.drawText(t)
    if "page9[signatureDeclaration]" in inputObj:
        if inputObj["page9[signatureDeclaration]"] == 'Applicant':
            can.circle(105, 508, 4, fill=1)
            s = can.beginText()
            s.setFont(customFont, customFontSize)
            name = inputObj['page9[confirmationApplicantName]']
            can.drawString(25, 480, name)
            address = inputObj['page9[confirmationApplicantAddress]']
            newAddress = "\n".join(wrap(address, 82))
            s.setTextOrigin(25, 450)
            s.textLines(newAddress)
            can.drawText(s)
        elif inputObj["page9[signatureDeclaration]"] == 'Representative':
            can.circle(184.5, 508, 4, fill=1)
            s = can.beginText()
            s.setFont(customFont, customFontSize)
            name = inputObj['page9[confirmationRepresentativeName]']
            can.drawString(25, 480, name)
            address = inputObj['page9[confirmationRepresentativeAddress]']
            newAddress = "\n".join(wrap(address, 82))
            s.setTextOrigin(25, 450)
            s.textLines(newAddress)
            can.drawText(s)
        else:
            print("no option selected in page9[signatureDeclaration]")

    barcodeMaker(self, tempInput[0], tempInput[1])

    drawing = svg2rlg(os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/results/'+tempInput[1]+'/barcode.svg'))
    renderPM.drawToFile(drawing, os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/results/'+tempInput[1]+'/barcode.png'), fmt="PNG")

    im = Image.open(os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/white-background.jpg'))
    side_im_data = io.BytesIO()
    im.save(side_im_data, format='png')
    side_im_data.seek(0)
    side_1out = ImageReader(side_im_data)
    can.drawImage(side_1out,315,35, width=270, height=150)

    bcodeIm = Image.open(os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/results/'+tempInput[1]+'/barcode.png'))
    side_bcodeIm_data = io.BytesIO()
    bcodeIm.save(side_bcodeIm_data, format='png')
    side_bcodeIm_data.seek(0)
    side_2out = ImageReader(side_bcodeIm_data)
    can.drawImage(side_2out,315,35, width=260, height=145)


    can.showPage()
    return can

def blankPageInputs(self, can):
    can.showPage()
    return can


def nextLineForPara(x, y, z):
    import math
    textLength = x;
    writeLength = y;
    spacing = z;
    totalSpacing = math.ceil(x/y)*z + z;
    return totalSpacing

def nextLineForPage12(x,y,z):
    import math
    textLength = x;
    writeLength = y;
    spacing = z;
    totalSpacing = math.ceil(x/y)*z + 2*z;
    return totalSpacing

def add_one_by_one(l):
    l = [int(i) for i in l] 
    new_l = []
    cumsum = 0
    for elt in l:
        cumsum += elt
        new_l.append(cumsum)
    new_l = [str(i) for i in new_l] 
    return new_l

def barcodeMaker(self, formInputs, applicantCode):
    from django.conf import settings
    import os
    from pdf417 import encode, render_image, render_svg
    text = formInputs

    # Convert to code words
    codes = encode(text)

    # Generate barcode as SVG
    svg = render_svg(codes)  # ElementTree object
    svg.write(os.path.join(settings.BASE_DIR, 'applicationForm/dataPreparation/results/'+applicantCode+'/barcode.svg'))
    

def sortDocumentsDate(self, inputObj):
    from datetime import datetime
    indexList = []
    dateList = inputObj[0]
    descList = inputObj[1]
    pageList = inputObj[2]
    list_of_dates= [datetime.strptime(date,"%Y-%m-%d") for date in dateList]
    dateListNew = [x for _,x in sorted(zip(list_of_dates, dateList))]
    descListNew = [x for _,x in sorted(zip(list_of_dates, descList))]
    pageListTemp = [x for _,x in sorted(zip(list_of_dates, pageList))]
    pageListNew = add_one_by_one(pageListTemp)
    return [dateListNew, descListNew, pageListNew, pageListTemp]

def bookmarkPageInputs(self, can, inputObj):
    title = inputObj[0] + " (" + inputObj[1] + " pages) "
    t1 = can.beginText()
    t1.setFont('Courier-Bold', 20)
    newPage = "\n".join(wrap(title, 40))
    t1.setTextOrigin(50, 600)
    t1.textLines(newPage)
    can.drawText(t1)
    can.showPage()
    return can

def anonymityDoc(self, can, inputObj):
    title = "Request of Anonymity"
    can.setFont('Courier-Bold', 20)
    can.drawString(180, 700, title)

    t = can.beginText()
    t.setFont(customFont, customFontSize)
    text = inputObj
    newText = "\n".join(wrap(text, 85))
    t.setTextOrigin(25, 640)
    t.textLines(newText)
    can.drawText(t)
    can.showPage()
    return can


def modifyCountryNames(initialName):
    tempList = initialName.split("(")
    return tempList[0]
