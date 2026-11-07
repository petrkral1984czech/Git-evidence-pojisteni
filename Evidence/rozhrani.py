from Evidence.evidence import Evidence
from evidence import Evidence

class Rozhrani:

    def __init__(self, evidence):
        self.evidence = evidence

    def nacti_text (self, vstup):     # načte text pro vstup od uživatele
        while True:
            vstup = input(vstup).strip()
            if vstup:
                return vstup
            print ("zadejte platný text, nesmí být pole prázdné\n")

    def nacti_cislo(self, vstup):    #načte číslko od uživatele pro věk a mobil
        while True:
            vstup = input(vstup).strip()
            if vstup.isdigit():
                return int(vstup)
            print("zadejte platné číslo, nesmí být pole prázdné\n")

    def nacti_jmeno_prijmeni(self):    # načte textovou hodnotu vstupu a předá do jména a příjmení
        jmeno = self.nacti_text("Zadejte jméno\n")
        prijmeni = self.nacti_text("Zadejte příjmení\n")
        return jmeno, prijmeni

    def pridej_pojistence(self):   # dodání nového pojištence
        jmeno, prijmeni = self.nacti_jmeno_prijmeni()
        vek = self.nacti_cislo("Zadejte věk\n")
        mobil = self.nacti_cislo("Zadejte telefonní číslo\n")

        self.evidence.pridat_pojisteneho(jmeno, prijmeni, vek, mobil)
        print(f"Pojistenec {jmeno} {prijmeni} byl úspěšně přidán.\n")
        input("zmáčkni klávesu pro pokračování")

    def vypis_pojistence(self):    #vypis všech údajů o pojištěncích
            pojistenci = self.evidence.vypis_pojistence()
            if not pojistenci:
                print("Žádní pojištěnci nebyli nalezeni.\n")

            else:
                print("Seznam pojištěnců:\n")


                for pojisteny in pojistenci:
                    print(pojisteny)

            input("zmáčkni klávesu pro pokračování")

    def vyhledej_pojistence(self):
        jmeno, prijmeni = self.nacti_jmeno_prijmeni()
        nalezeni_pojistenci = self.evidence.vyhledej_pojistence(jmeno, prijmeni)

        if not nalezeni_pojistenci:
            print(f"Pojištěnec {jmeno} {prijmeni} nebyl nalezen v evidenci.\n")
        else:
            print(f"Nalezení pojištěnci {jmeno} {prijmeni}:\n")
            for pojisteny in nalezeni_pojistenci:
                print(pojisteny)

        input("zmáčkni klávesu pro pokračování")

    def smaz_pojistence(self):              # maže pojištence dle jmén a příjmení
        print ("**** Mazání pojištěnce ****\n")
        jmeno, prijmeni = self.nacti_jmeno_prijmeni()
        byl_smazan = self.evidence.smaz_pojistence(jmeno,prijmeni)

        if byl_smazan > 0:
            print(f"Pojištěnec {jmeno} {prijmeni} byl úspěšně smazán z evidence.\n")
        else:
            print(f"Pojištěnec {jmeno} {prijmeni} nebyl nalezen v evidenci.\n")


    def spust(self):
        while True:
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("                Evidence pojištěnců")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

            print("Vyberte akci:")
            print("1. Přidat pojištěnce")
            print("2. Vypsat všechny pojištěnce")
            print("3. Vyhledat pojištěnce")
            print("4. Smazat pojištěnce")
            print("5. Konec programu")

            volba = input(" ").strip()

            match volba:

                case "1":
                    self.pridej_pojistence()
                case "2":
                    self.vypis_pojistence()
                case "3":
                    self.vyhledej_pojistence()
                case "4":
                    self.smaz_pojistence()
                case "5":
                    print("Děkujeme za použití evidence pojištěnců. Program bude ukončen.")
                    break
                case _:
                    print("Neplatná volba. Zadejte číslo od 1 do 5.\n")









