def firstPageInputs(self, can, inputObj):
    can.drawString(30, 420, inputObj["page2[indSurname]"])
    can.drawString(30, 380, inputObj["page2[indFirstName]"])
    baseX = 27
    birthdate = inputObj["page2[birthDate]"]
    for i in birthdate.replace('/', ''):
        baseY = 340
        can.drawString(baseX, baseY, i)
        baseX = baseX+17

    can.drawString(30, 300, inputObj["page2[indPob]"])
    can.drawString(30, 260, inputObj["page2[indNationality]"])
    can.drawString(30, 260, inputObj["page2[indNationality]"])
    can.showPage()
    return can


def secondPageInputs(self, can, inputObj):
    can.drawString(30, 420, "hahahahahhaa")
    can.showPage()
    return can
