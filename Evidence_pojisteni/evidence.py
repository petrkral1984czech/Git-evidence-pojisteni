from pojisteni import Pojisteny

""""
 tady se vše eviduje a ukládá - databáze
"""

class Evidence:

    def __init__(self):
        self._pojisteni = []

    def pridej_pojistence(self, jmeno, prijmeni, vek, mobil):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, mobil)
        self._pojisteni.append(pojisteny)  # pojisteného  přidá  do seznamu

    def vypis_pojistence(self):
        return self._pojisteni

    def vyhledej_pojistence(self, jmeno, prijmeni):
        vrat_jmeno = jmeno.lower().strip()
        vrat_prijmeni = prijmeni.lower().strip()
        seznam_jmen = []

        for i in self._pojisteni:
            if i.jmeno.lower().strip() == vrat_jmeno and i.prijmeni.lower().strip() == vrat_prijmeni:
                seznam_jmen.append(i)

        return seznam_jmen
    