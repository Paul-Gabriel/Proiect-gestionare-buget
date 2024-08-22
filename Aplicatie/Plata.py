class Plata:
    def __init__(self,tip="-",valoare="-",data="-"):
        self.tip=tip
        self.valoare=float(valoare)
        self.data=data

    def __str__(self):
        return f"Tip: {self.tip}, Valoare: {self.valoare} lei, Data: {self.data}"
