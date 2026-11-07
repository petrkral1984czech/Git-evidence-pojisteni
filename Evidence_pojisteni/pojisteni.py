class Pojisteny:
# inicializuje osobu a vlastně jí tím dává atributy ( vlastnosti)

    def __init__(self, jmeno, prijmeni, vek, mobil):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobil = mobil

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, věk: {self.vek}, mobil: {self.mobil}"
