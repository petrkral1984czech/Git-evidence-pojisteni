from Evidence.evidence import Evidence
from evidence import Evidence

class Rozhrani:

    def __init__(self, evidence):
        self.evidence = evidence

    def nacti_text (self, vstup):     # načte text pro vstup od uživatele
        while True:
            vyzva = input(vstup).strip()
            if not vyzva:
                print("Zadejte text, nikoliv   prázdné pole.\n") # kontroluje zda bylo zadána hodnota nebo nic

            elif any(char.isdigit() for char in vyzva):  # kontroluje zda je text bez čísla
                print ("Zadejte text bez čísel\n")
            else:
                return vyzva

    def nacti_cislo(self, vstup):    #načte číslko od uživatele pro věk a mobil
        while True:
            vstup = input(vstup).strip()
            vstup_bez_textu = vstup.replace(" ", "")
            if not vstup:
                print("Zadejte číslo a ne prázdné pole\n")
            elif not vstup_bez_textu.isdigit():
                print ("Zadejte číslo bez použité textu a záporných hodnot\n")
            else:
                return (vstup)




    def nacti_jmeno_prijmeni(self):    # načte textovou hodnotu vstupu a předá do jména a příjmení
        jmeno = self.nacti_text("Zadejte jméno\n").title()     # nacte text do jmána a title by mělo udělat první písmeno velké a další již malá
        prijmeni = self.nacti_text("Zadejte příjmení\n").title()  # naste text do prijmeni a melo by udělat první písmeno velke a další malá
        return jmeno, prijmeni

    def pridej_pojistence(self):   # dodání nového pojištence
        jmeno, prijmeni = self.nacti_jmeno_prijmeni()
        vek = self.nacti_cislo("Zadejte věk\n")
        mobil_nacti = self.nacti_cislo("Zadejte telefonní číslo\n")
        mobil_uprav = str(mobil_nacti).replace(" ", "")  # převod na text a odmazání mezer
        mobil = f"{mobil_uprav[:3]} {mobil_uprav[3:6]} {mobil_uprav[6:]}"  # upravím formát na mobilní 111 222 333 pro čitelnost


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

        input("zmáčkni klávesu pro pokračování")


    def spust(self):    #spustí výběr akce pro uživatele co chtějí udělat s evidencí
        volba = ""
        while volba != "5":
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("                Evidence pojištěnců")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

            print("Vyberte akci:")
            print("1. Přidat pojištěnce")
            print("2. Vypsat všechny pojištěnce")
            print("3. Vyhledat pojištěnce")
            print("4. Smazat pojištěnce")
            print("5. Konec programu")

            volba = input(" \n").strip()

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









