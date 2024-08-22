from Plata import Plata

class Venit:
    def __init__(self, baniAlocati):
        self.baniAlocati = baniAlocati
        self.listaPlati = []

    def adaugaPlata(self, plata):
        self.listaPlati.append(plata)
        # print(f"Plata de {plata.valoare} lei pentru {plata.tip} a fost adăugată cu succes.")
    
    def getBaniAlocati(self):
        return self.baniAlocati

    def getBaniConsumati(self):
        return sum(map(lambda p: p.valoare, self.listaPlati))

    def getBaniRamasi(self):
        return self.getBaniAlocati() - self.getBaniConsumati()
    
    def sorteazaPlati(self, criteriu, ordonare=False):
        if criteriu == "tip":
            self.listaPlati.sort(key=lambda p: p.tip, reverse=ordonare)
        elif criteriu == "valoare":
            self.listaPlati.sort(key=lambda p: p.valoare, reverse=ordonare)
        elif criteriu == "data":
            self.listaPlati.sort(key=lambda p: p.data, reverse=ordonare)
        else:
            print("Criteriu necunoscut. Plățile nu au fost sortate.")

    def __str__(self):
        plati_str = "\n".join([str(plata) for plata in self.listaPlati])
        return (f"Bani alocați: {self.getBaniAlocati()} lei\n"
                f"Bani consumați: {self.getBaniConsumati()} lei\n"
                f"Bani ramasi: {self.getBaniRamasi()} lei\n"
                f"Plati:\n{plati_str if plati_str else 'Nicio plata efectuata.'}")
