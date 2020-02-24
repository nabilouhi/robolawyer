from textwrap import wrap
from reportlab.graphics import shapes
from .countryCoordDict import coordinateDict


def firstPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont('Helvetica', 10)

    if inputObj["page2[applicantType]"] == "Individual":
    
        can.drawString(30, 420, inputObj["page2[indSurname]"])
        can.drawString(30, 380, inputObj["page2[indFirstName]"])
        baseX = 27
        birthdate = inputObj["page2[birthDate]"]
        for i in birthdate.replace('/', ''):
            baseY = 340
            can.drawString(baseX, baseY, i)
            baseX = baseX+17

        
        can.drawString(30, 285, inputObj["page2[indPob]"])
        can.drawString(30, 245, inputObj["page2[indNationality]"])

        addressOne = inputObj["page2[indAddress]"]
        addressOneLength = len(addressOne)
        newAddress = "\n".join(wrap(addressOne, 55))
        t.setTextOrigin(30, 205)
        t.textLines(newAddress)
        can.drawText(t)

        can.drawString(30, 110, inputObj["page2[indPhone]"])
        can.drawString(30, 70, inputObj["page2[indEmail]"])

        if "page2[applicantSex]" in inputObj:
            if  inputObj["page2[applicantSex]"] == 'Male':
                can.circle(78,46, 4, fill=1)
            elif inputObj["page2[applicantSex]"] == 'Female':
                can.circle(148, 46, 4, fill=1)
        else:
            print("no value entered")

        

    else:
        can.drawString(30, 285, "")
        can.drawString(30, 245, "")
        nameOne = inputObj["page2[orgName]"]
        newNameOne = "\n".join(wrap(nameOne, 55))
        t.setTextOrigin(310, 420)
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
        newAddressTwo = "\n".join(wrap(addressTwo, 55))
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
    t = can.beginText()
    t.setFont('Helvetica', 10)
    if inputObj["page3[indRepresentativeType]"] == "non-lawyer":
        can.drawString(30, 662, inputObj["page3[indNLCapacity]"])
        can.drawString(30, 622, inputObj["page3[indNLSurname]"])
        can.drawString(30, 581, inputObj["page3[indNLFirstName]"])
        can.drawString(30, 544, inputObj["page3[indNLNationality]"])
        addressThree = inputObj["page3[indNLAddress]"]
        addressThreeLength = len(addressThree)
        newAddress = "\n".join(wrap(addressThree, 55))
        t.setTextOrigin(30, 503)
        t.textLines(newAddress)
        can.drawText(t)
        can.drawString(30, 402, inputObj["page3[indNLEmail]"])
        can.drawString(30, 362, inputObj["page3[indNLTel]"])
        can.drawString(30, 322, inputObj["page3[indNLFax]"])

    elif inputObj["page3[indRepresentativeType]"] == "lawyer":
        can.drawString(310, 662, inputObj["page3[indLSurname]"])
        can.drawString(310, 622, inputObj["page3[indLFirstName]"])
        can.drawString(310, 581, inputObj["page3[indLNationality]"])
        addressFour = inputObj["page3[indLAddress]"]
        newAddressFour = "\n".join(wrap(addressFour, 55))
        t.setTextOrigin(310, 543)
        t.textLines(newAddressFour)
        can.drawText(t)
        can.drawString(310, 402, inputObj["page3[indLEmail]"])
        can.drawString(310, 362, inputObj["page3[indLTel]"])
        can.drawString(310, 322, inputObj["page3[indLFax]"])
        can.drawString(30, 37, inputObj["page3[indIndeComms]"])
    
    else:
        can.drawString(30, 37, inputObj["page3[indIndeCommsSelf]"])

    can.showPage()

    return can

def fourthPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont('Helvetica', 10)
    if inputObj["page3[orgRepresentativeType]"] == "non-lawyer":
        can.drawString(30, 662, inputObj["page3[orgnlCapacity]"])
        can.drawString(30, 622, inputObj["page3[orgnlSurname]"])
        can.drawString(30, 581, inputObj["page3[orgnlFirstName]"])
        can.drawString(30, 544, inputObj["page3[orgnlNationality]"])
        addressFour = inputObj["page3[orgnlAddress]"]
        newAddressFour = "\n".join(wrap(addressFour, 55))
        t.setTextOrigin(30, 503)
        t.textLines(newAddressFour)
        can.drawText(t)
        can.drawString(30, 402, inputObj["page3[orgnlEmail]"])
        can.drawString(30, 362, inputObj["page3[orgnlTel]"])
        can.drawString(30, 322, inputObj["page3[orgnlFax]"])

    elif inputObj["page3[orgRepresentativeType]"] == "lawyer":
        can.drawString(310, 662, inputObj["page3[orglSurname]"])
        can.drawString(310, 622, inputObj["page3[orglFirstName]"])
        can.drawString(310, 581, inputObj["page3[orglNationality]"])
        addressFive = inputObj["page3[orglAddress]"]
        newAddressFive = "\n".join(wrap(addressFive, 55))
        t.setTextOrigin(310, 543)
        t.textLines(newAddressFive)
        can.drawText(t)
        can.drawString(310, 402, inputObj["page3[orglEmail]"])
        can.drawString(310, 362, inputObj["page3[orglTel]"])
        can.drawString(310, 322, inputObj["page3[orglFax]"])
        can.drawString(30, 37, inputObj["page3[orgIndeComms]"])
    
    else:
        can.drawString(30, 37, inputObj["page3[indIndeCommsSelf]"])

    can.showPage()
    return can


def fifthPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont('Helvetica', 11)
    stOfFactsText = inputObj
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 109))
    t.setTextOrigin(30, 670)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def sixthPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont('Helvetica', 11)
    stOfFactsText = inputObj
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 109))
    t.setTextOrigin(30, 760)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def seventhPageInputs(self, can, inputObj):
    t = can.beginText()
    t.setFont('Helvetica', 11)
    stOfFactsText = inputObj
    newStOfFactsText = "\n".join(wrap(stOfFactsText, 109))
    t.setTextOrigin(30, 760)
    t.textLines(newStOfFactsText)
    can.drawText(t)
    can.showPage()
    return can

def eighthPageInputs(self, can, inputObj):
    yCoord = 750
    for item in range(len(inputObj[0])):
        t1 = can.beginText()
        t1.setFont('Helvetica', 11)
        if len(inputObj[0]) > 1:
            article = inputObj[0][item]
            articleExp = inputObj[1][item]
        elif len(inputObj[0]) == 1:
            article = inputObj[0][0]
            articleExp = inputObj[1][0]
        else:
            print("error reported in EighthPageInputs")

        newArticle = "\n".join(wrap(article, 10))
        t1.setTextOrigin(30, yCoord)
        t1.textLines(newArticle)
        can.drawText(t1)

        t2 = can.beginText()
        t2.setFont('Helvetica', 11)
        newArticleExp = "\n".join(wrap(articleExp, 70))
        t2.setTextOrigin(200, yCoord)
        t2.textLines(newArticleExp)
        can.drawText(t2)
        yCoord -= nextLineForPara(len(articleExp), 70, 11)

    can.showPage()
    return can

def ninthPageInputs(self, can, inputObj):
    can.showPage()
    return can

def tenthPageInputs(self, can, inputObj):
    yCoord = 705
    for item in range(len(inputObj[0])):
        t1 = can.beginText()
        t1.setFont('Helvetica', 11)
        if len(inputObj[0]) > 1:
            complain = inputObj[0][item]
            remedies = inputObj[1][item]
        elif len(inputObj[0]) == 1:
            complain = inputObj[0][0]
            remedies = inputObj[1][0]
        else:
            print("error reported in TenthPageInputs")

        newComplain = "\n".join(wrap(complain, 30))
        t1.setTextOrigin(30, yCoord)
        t1.textLines(newComplain)
        can.drawText(t1)

        # t2 = can.beginText()
        # t2.setFont('Helvetica', 11)
        # newComplainDate = "\n".join(wrap(complainDate, 15))
        # t2.setTextOrigin(200, yCoord)
        # t2.textLines(newComplainDate)
        # can.drawText(t2)

        t2 = can.beginText()
        t2.setFont('Helvetica', 11)
        newRemedy = "\n".join(wrap(remedies, 70))
        t2.setTextOrigin(190, yCoord)
        t2.textLines(newRemedy)
        can.drawText(t2)
        yCoord -= nextLineForPara(len(newRemedy), 70, 11)

    can.showPage()
    return can

def eleventhPageInputs(self, can, inputObj, secondInput):
    if "page6[appealAvailable]" in inputObj:
            if  inputObj["page6[appealAvailable]"] == 'Yes':
                can.circle(466,787, 4, fill=1)
                t = can.beginText()
                t.setFont('Helvetica', 11)
                appealDescribe = inputObj['page6[appealDescribe]']
                newAppealDescribe = "\n".join(wrap(appealDescribe, 109))
                t.setTextOrigin(30, 732)
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
                t.setFont('Helvetica', 11)
                intInvestigationDesc = secondInput['page7[intInvestigationDesc]']
                newIntInvestigationDesc = "\n".join(wrap(intInvestigationDesc, 109))
                t.setTextOrigin(30, 390)
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
                t.setFont('Helvetica', 11)
                prevAppDesc = secondInput['page7[prevAppDesc]']
                newPrevAppDesc = "\n".join(wrap(prevAppDesc, 109))
                t.setTextOrigin(30, 75)
                t.textLines(newPrevAppDesc)
                can.drawText(t)
            elif secondInput["page7[prevApplications]"] == 'No':
                can.circle(466.2, 110, 4, fill=1)
            else:
                print("no value entered")
    
    can.showPage()
    return can

def twelvthPageInputs(self, can, inputObj):
    print(inputObj)
    # for dates in inputObj[0]:

    can.showPage()
    return can

def thirteenthPageInputs(self, can, inputObj):
    can.showPage()
    return can

def blankPageInputs(self, can, inputObj):
    can.showPage()
    return can


def nextLineForPara(x, y, z):
    import math
    textLength = x;
    writeLength = y;
    spacing = z;
    totalSpacing = math.ceil(x/y)*z + 3*z;
    return totalSpacing

def barcodeMaker(self, formInputs):
    from pdf417 import encode, render_image, render_svg
    text = formInputs

    # Convert to code words
    codes = encode(text)

    # Generate barcode as image
    image = render_image(codes)  # Pillow Image object
    image.save('barcode.jpg')

    # Generate barcode as SVG
    svg = render_svg(codes)  # ElementTree object
    svg.write("barcode.svg")
    