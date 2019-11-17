# script to run when updating this API

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
                        proceedingType=row['ProceedingType'],
                        court=row['Court'])
        p.save()


if __name__ == "__main__":
    print("data updated")
    pass
