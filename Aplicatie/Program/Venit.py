from Program.Plata import Plata

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
    
    def sorteazaPlati(self, criteriu="data", ordonare=False, lista_plati=None):
        if lista_plati is None:
            lista_plati = self.listaPlati

        if criteriu == "tip":
            lista_plati.sort(key=lambda p: p.tip, reverse = ordonare)
        elif criteriu == "valoare":
            lista_plati.sort(key=lambda p: p.valoare, reverse = ordonare)
        elif criteriu == "data":
            lista_plati.sort(key=lambda p: p.data, reverse = ordonare)
        else:
            print("Criteriu necunoscut. Plățile nu au fost sortate.")

        return lista_plati

    def afisarePlatiDupaCriteriu(self, criteriu1, criteriu2, lista_plati=None):
        if lista_plati is None:
            lista_plati = self.listaPlati
        
        if criteriu1 == "tip":
            for plata in lista_plati:
                if criteriu2 == plata.tip:
                    print(plata)
        elif criteriu1 == "valoare":
            for plata in lista_plati:
                if criteriu2 == plata.valoare:
                    print(plata)
        elif criteriu1 == "data":
            for plata in lista_plati:
                if criteriu2 == str(plata.data.strftime("%Y-%m-%d")):
                    print(plata)
        else:
            print("Criteriu necunoscut. Plățile nu au fost sortate.")

    def __str__(self):
        plati_str = "\n".join([str(plata) for plata in self.listaPlati])
        return (f"Bani alocați: {self.getBaniAlocati()} lei\n"
                f"Bani consumați: {self.getBaniConsumati()} lei\n"
                f"Bani ramasi: {self.getBaniRamasi()} lei\n"
                f"Plati:\n{plati_str if plati_str else 'Nicio plata efectuata.'}")
