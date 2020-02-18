from textwrap import wrap
from reportlab.graphics import shapes


def firstPageInputs(self, can, inputObj):
    print(inputObj)
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
    can.drawString(30, 420, "hahahahahhaa")
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
