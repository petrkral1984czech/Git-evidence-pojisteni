from pojisteni import Pojisteny


class Evidence:
    def __init__(self):
        self._pojisteni = []

    def pridat_pojisteneho(self, jmeno, prijmeni, vek, mobil):  # přidá nového pojistence
        pojisteny = Pojisteny(jmeno, prijmeni, vek, mobil)
        self._pojisteni.append(pojisteny)

    def vypis_pojistence(self):    # vrátí seznam pojistenců
        return self._pojisteni

    def vyhledej_pojistence(self, jmeno, prijmeni):
        vrat_jmeno = jmeno.lower().strip()
        vrat_prijmeni = prijmeni.lower().strip()

        return [
            p for p in self._pojisteni
            if p.jmeno.lower().strip() == vrat_jmeno and p.prijmeni.lower().strip() == vrat_prijmeni
        ]

    def smaz_pojistence(self, jmeno, prijmeni):
        vrat_jmeno = jmeno.lower()
        vrat_prijmeni = prijmeni.lower()
        pocet_puvodni = len(self._pojisteni)

        self._pojisteni = [
            p for p in self._pojisteni
                if not (p.jmeno.lower() == vrat_jmeno and p.prijmeni.lower() == vrat_prijmeni)
        ]

        return len(self._pojisteni) < pocet_puvodni
