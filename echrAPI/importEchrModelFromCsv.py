# script to run when updating this API

from echrAPI.models import EchrDetail
import csv
import os


filename = "Ratification of ECHR dates and coutries.csv"
path = "C:/Personal_DS/robo/robolawyer-project/echrAPI"

os.chdir(path)
with open(filename) as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        p = EchrDetail(country=row['Country'],
                       ratDate=row['Ratification date'])
        p.save()


if __name__ == "__main__":
    print("data updated")
