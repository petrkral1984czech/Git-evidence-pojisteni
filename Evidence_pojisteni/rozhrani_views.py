from evidence import Evidence
from pojisteni import Pojisteny

"""													
tenhle soubor komunikuje s uživatelem													
"""

class Rozhrani:  # založím třídu  Rozhraní

    def __init__(self, evidence):
        self.evidence = evidence

    def _nacti_text(self, vyzva):  # slouží k načtení textu, měl by upbrat mezery ze vstupu
        while True:
            vstup = input(vyzva).strip()
            if vstup:
                return vstup
            print("Zadejte prosím text. Hodnota nesmí být prázdná.")

    def _nacti_cislo(self, vyzva):  # tahle metoda načte číslo a odstraní mezery
        while True:
            vstup = input(vyzva).strip()
            if vstup.isdigit():
                return int(vstup)
            print("Zadejte prosím číslo")

    def _nacti_jmeno_prijmeni(self):  # načte jmeno a příjmení bez mezer
        jmeno = self._nacti_text("Zadejte jméno: \n")
        prijmeni = self._nacti_text("Zadejte příjmení: \n")
        return jmeno, prijmeni

    def pridej_pojistence(self):  # tahle metoda přidá pojištěnce
        jmeno = self._nacti_text("Zadejte jméno: \n")
        prijmeni = self._nacti_text("Zadejte příjmení: \n")
        vek = self._nacti_cislo("Zadejte věk: \n")
        mobil = self._nacti_text("Zadejte mobilní číslo: \n")

        self.evidence.pridej_pojistence(jmeno, prijmeni, vek, mobil)
        print(f"Pojištěnec {jmeno} {prijmeni} byl úspěšně přidán.\n")
        print("Pokračujte libovolnou klávesou...")
        input()

    def vypis_pojistence(self):
        pojistenci = self.evidence.vypis_pojistence()
        if not pojistenci:
            print("Zatím neexistují žádní pojištěnci.\n")  # pokud je seznam prázdný, vypíše se hláška
        else:
            print("Seznam pojištěnců:\n")
            for pojisteny in pojistenci:
                print(pojisteny)

        print("Pokračujte libovolnou klávesou...")
        input()

    def vyhledej_pojistence(self):
        jmeno, prijmeni = self._nacti_jmeno_prijmeni()
        nalezeni_pojistenci = self.evidence.vyhledej_pojistence(jmeno, prijmeni)

        if not nalezeni_pojistenci:
            print(f"Pojištěnec {jmeno} {prijmeni} nebyl nalezen.\n")
        else:
            print(f"Nalezení pojištěnci pro {jmeno} {prijmeni}:")
            for pojisteny in nalezeni_pojistenci:
                print(pojisteny)

        print("Pokračujte libovolnou klávesou...")
        input()

    def spust(self):  # tady spustím rozhraní pro uživatele, aby mohl zadávat příkazy

        while True:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("                         Evidence pojištených osob ")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("")
            print("Vyberte požadovanou akci:")
            print("1 - Přidat nového pojištěnce")
            print("2 - Vypsat všechny pojištěnce")
            print("3 - Vyhledat pojištěnce")
            print("4 - Konec programu\n")

            volba = input().strip()

            match volba:

                case "1":
                    self.pridej_pojistence()
                case "2":
                    self.vypis_pojistence()
                case "3":
                    self.vyhledej_pojistence()
                case "4":
                    print("Konec programu.\n")
                    break
                case _:  # varianta pro  neplatnou volbu u case místo else co se užívá u IF
                    print("Neplatná volba. Zadejte číslo od 1 do 4.\n")
