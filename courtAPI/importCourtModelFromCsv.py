# script to run when updating this API
# use python manage.py shell for updating

from courtAPI.models import CourtDetail
import csv
import os


filename = "Countries_and_national_courts.csv"
path = "C:/Personal_DS/robo/robolawyer-project/courtAPI"

os.chdir(path)
with open(filename, encoding="UTF-8") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        p = CourtDetail(country=row['Country'],
                        proceedingType1=row['ProceedingType1'],
                        court1=row['Court1'],
                        proceedingType2=row['ProceedingType2'],
                        court2=row['Court2'],
                        proceedingType3=row['ProceedingType3'],
                        court3=row['Court3'])
        print(p)
        p.save()


if __name__ == "__main__":
    print("data updated")
