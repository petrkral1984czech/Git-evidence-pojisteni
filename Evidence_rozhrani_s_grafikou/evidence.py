import json
import os
from pojistenci import Pojisteny

class Evidence:
    def __init__(self, soubor="pojistenci.json"):    # nastaví a načte JSON soubor a nachystá prázdný seznam kam se zapíší data souboru
        self._pojisteni = []
        self._soubor = soubor
        self._nacti_ze_souboru()

    def _nacti_ze_souboru(self):    # načte soubor a pokud ne pak
        if not os.path.exists(self._soubor):
            self._pojisteni = []
            return

        with open(self._soubor, "r", encoding="utf-8") as f:
            obsah = f.read().strip()

        if not obsah:
            self._pojisteni = []
            return

        data = json.loads(obsah)      # vznikne proměná data z načteného json souboru upraveného v obsah =
        self._pojisteni = [Pojisteny.from_dict(polozka) for polozka in data]   # změní na seznam slovníků  a vytvoří objekt Pojisteny

    def _uloz_soubor(self):         # uloží soubor jako json, "w" přepíše soubor novými údaji, dump - převede objekt na data; ensure - čitelnost diakritiky a indent - formátování
        data = [p.to_dict() for p in self._pojisteni]
        with open(self._soubor, "w", encoding="utf-8") as f:
            json.dump(data, f,  ensure_ascii=False, indent=2)

    def _dalsi_id(self):
        cisla_id =  []
        for p in self._pojisteni:
            if p in self._pojisteni is not None:
                try:
                    cisla_id.append(int(p.id))
                except (ValueError, TypeError):
                    pass
        return max(cisla_id, default=0) +1


    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):  # přidá nového pojistence
        nove_id = self._dalsi_id()
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon, id=nove_id)
        self._pojisteni.append(pojisteny)
        self._uloz_soubor()


    def vypis_pojistence(self):  # vrátí seznam pojistenců
        return self._pojisteni

    def vyhledej_pojistence(self, jmeno, prijmeni):
        vrat_jmeno = jmeno.lower().strip()
        vrat_prijmeni = prijmeni.lower().strip()

        return [
            p for p in self._pojisteni
            if p.jmeno.lower().strip() == vrat_jmeno and p.prijmeni.lower().strip() == vrat_prijmeni
        ]

    def smaz_pojistence(self, jmeno, prijmeni):
        vrat_jmeno = jmeno.lower().strip()
        vrat_prijmeni = prijmeni.lower().strip()
        pocet_puvodni = len(self._pojisteni)

        self._pojisteni = [
            p for p in self._pojisteni
            if not (p.jmeno.lower().strip() == vrat_jmeno and p.prijmeni.lower().strip() == vrat_prijmeni)
        ]
        smazano = len(self._pojisteni) < pocet_puvodni
        if smazano:
            self._uloz_soubor()
        return smazano

