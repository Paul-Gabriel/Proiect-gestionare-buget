import csv
from Venit import Venit

class Buget:
    def __init__(self,venit):
        self.venit=venit
        self.venitFondEconomii=Venit(venit*20/100)
        self.venitNevoi=Venit(venit*50/100)
        self.venitDorinte=Venit(venit*30/100)

    def afisareVenit(self):
        print(f"Venitul lunar este de: {self.venit} lei.\n")

    def afisareVenitPeTip(self):
        print(f"Venit fond economii: {self.venitFondEconomii.getBaniAlocati()} \nVenit nevoi: {self.venitNevoi.getBaniAlocati()} \nVenit dorinte: {self.venitDorinte.getBaniAlocati()} \n")

    def combinaPlati(self):
        return self.venitFondEconomii.listaPlati + self.venitNevoi.listaPlati + self.venitDorinte.listaPlati

    def salvareInCSV3(self):
        with open('C:\\Users\\paul1\\Desktop\\Proiect gestionare buget\\Aplicatie\\Fisiere_CSV\\platiSalvateSeparat.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(['Plati nevoi:'])
            writer.writerow(['tip', 'valoare', 'data'])
            if(self.venitNevoi.listaPlati):
                for plata in self.venitNevoi.listaPlati:
                    writer.writerow([plata.tip, plata.valoare, plata.data.strftime('%Y-%m-%d')])
            else:
                writer.writerow(['Nicio plata efectuata.'])
            
            writer.writerow(['Plati dorinte:'])
            writer.writerow(['tip', 'valoare', 'data'])
            if(self.venitDorinte.listaPlati):
                for plata in self.venitDorinte.listaPlati:
                    writer.writerow([plata.tip, plata.valoare, plata.data.strftime('%Y-%m-%d')])
            else:
                writer.writerow(['Nicio plata efectuata.'])

            writer.writerow(['Plati fond de economi:'])
            writer.writerow(['tip', 'valoare', 'data'])
            if(self.venitFondEconomii.listaPlati):
                for plata in self.venitFondEconomii.listaPlati:
                    writer.writerow([plata.tip, plata.valoare, plata.data.strftime('%Y-%m-%d')])
            else:
                writer.writerow(['Nicio plata efectuata.'])

    def salvareInCSV(self):
        with open('C:\\Users\\paul1\\Desktop\\Proiect gestionare buget\\Aplicatie\\Fisiere_CSV\\platiSalvate.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['tip', 'valoare', 'data'])
            if(self.combinaPlati()):
                for plata in self.combinaPlati():
                    writer.writerow([plata.tip, plata.valoare, plata.data.strftime('%Y-%m-%d')])
            else:
                writer.writerow(['Nicio plata efectuata.'])

    def __str__(self):
        return (f"Buget total: {self.venit} lei\n\n"
                f"Fond Economii:\n{self.venitFondEconomii}\n\n"
                f"Fond Nevoi:\n{self.venitNevoi}\n\n"
                f"Fond Dorințe:\n{self.venitDorinte}\n")
