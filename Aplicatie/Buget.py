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

    def __str__(self):
        return (f"Buget total: {self.venit} lei\n\n"
                f"Fond Economii:\n{self.venitFondEconomii}\n\n"
                f"Fond Nevoi:\n{self.venitNevoi}\n\n"
                f"Fond Dorințe:\n{self.venitDorinte}\n")
