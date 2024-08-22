from datetime import date
from Buget import Buget
from Venit import Venit
from Plata import Plata
import csv

def prelucrareCSV(buget):
    
    with open('C:\\Users\\paul1\\Desktop\\Proiect gestionare buget\\Aplicatie\\dateNevoi.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            buget.venitNevoi.adaugaPlata(Plata(lines[0],lines[1],lines[2]))

    with open('C:\\Users\\paul1\\Desktop\\Proiect gestionare buget\\Aplicatie\\dateDorinte.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            buget.venitDorinte.adaugaPlata(Plata(lines[0],lines[1],lines[2]))

    with open('C:\\Users\\paul1\\Desktop\\Proiect gestionare buget\\Aplicatie\\dateFondEconomii.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            buget.venitFondEconomii.adaugaPlata(Plata(lines[0],lines[1],lines[2]))

    # buget.venitNevoi.sorteazaPlati("valoare")
    # print(buget)

    # buget.venitNevoi.sorteazaPlati("data",True)
    # print(buget)


def main():
    buget=Buget(1000)
    prelucrareCSV(buget)
    # print(buget)

    buget.salvareInCSV()
    buget.salvareInCSV3()

    # buget.venitNevoi.sorteazaPlati("data",True,buget.combinaPlati)

    for plata in buget.combinaPlati():
        print(plata)
    

if __name__ == "__main__":
    main()
