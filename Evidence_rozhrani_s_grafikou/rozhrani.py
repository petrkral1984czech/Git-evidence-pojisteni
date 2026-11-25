import html
from pathlib import Path
from flask import Flask, request, redirect, url_for

class Rozhrani:
    def __init__(self, evidence, sablona="index.html"):
        self.evidence = evidence
        self.sablona = sablona
        self.app = Flask(__name__)
        self._zaregistruj_routy()

    def _seznam_na_html(self, osoby, prazdny_text):  # mění seznam objektu na HTML kod seznamu pro vložení do vykreslit..., převadí vše na text a formátuje
        if not osoby:
            return f"<p>{html.escape(prazdny_text)}</p>"

        polozky = [
            "<li>"
            f"{html.escape(str(p.id))} {html.escape(str(p.jmeno))} {html.escape(str(p.prijmeni))}"
            f" věk: {html.escape(str(p.vek))}, tel: {html.escape(str(p.telefon))}"
            "</li>"
            for p in osoby
        ]
        return "<ul>" + "".join(polozky) + "</ul>"

    def _vykresli(self, obsah=""):  # najde cestu k souboru šablony tj. index.html a do OBSAH vykresly u vyhledat informace pro vypsaní
        cesta_sablony = Path(__file__).resolve().parent / "templates" / self.sablona
        kod_stranky = cesta_sablony.read_text(encoding="utf-8")
        return kod_stranky.replace("[[OBSAH]]",obsah)

    def _zaregistruj_routy(self):    # řekne flasku kam vracet routy tj IP adresu a navazující s /pridat.../vyhledat...a vola self.vykresli
        @self.app.get("/")
        def index():
            return self._vykresli()

        @self.app.post("/pridat")       ## ukol je pridat nového pojistence : kontroluje vstupní data a kominikace s prohlížečem, příprava dat pro evidence-pridaní
        def pridat():
            jmeno = request.form.get("jmeno", "").strip().title()
            prijmeni = request.form.get("prijmeni", "").strip().title()
            vek = request.form.get("vek", "").strip()
            telefon_neformatovan = request.form.get("telefon", "").strip().replace(" ", "")
            telefon = f"{telefon_neformatovan[:3]} {telefon_neformatovan[3:6]} {telefon_neformatovan[6:]}"
            if jmeno and prijmeni and vek.isdigit() and telefon:
                self.evidence.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
                zprava = (f"<p>Pojištěnec {html.escape(jmeno)} {html.escape(prijmeni)} {html.escape(telefon)} byl úspěšně přidán </p>")
            else:
                zprava = "<p> Vyplňte prosím platné údaje</p>"

            return self._vykresli(zprava)

        @self.app.route("/vyhledat", methods=["GET", "POST"])
        def vyhledat():                                     # příprava dat pro vyhledání
            jmeno = request.form.get("jmeno", "").strip().title()
            prijmeni = request.form.get("prijmeni", "").strip().title()
            nalezeni = self.evidence.vyhledej_pojistence(jmeno, prijmeni)
            obsah_hledani = ("<h2> VÝSLEDKY VYHLEDÁVÁNÍ: </h2>"
            + self._seznam_na_html(nalezeni, "Nikdo nebyl nalezen"))
            return self._vykresli(obsah_hledani)


        @self.app.route("/smazat", methods=["GET", "POST"])
        def smazat():   # komunikace s prohlížečem a příprava dat pro smazání v evidence
            jmeno = request.form.get("jmeno", "").strip().title()
            prijmeni = request.form.get("prijmeni", "").strip().title()
            smazano = self.evidence.smaz_pojistence(jmeno, prijmeni)
            if smazano:
                zprava_smazat = (
                f"<p>Pojištěnec {html.escape(jmeno)} {html.escape(prijmeni)} byl smazán z databáze </p>")
            else:
                zprava_smazat = "<p> Uživatel není smazán </p>"
            return self._vykresli(zprava_smazat)

        @self.app.route("/vse", methods=["GET", "POST"])
        def vse():  # pomůže připravit data pro evidence
          seznam = self.evidence.vypis_pojistence()
          obsah_vsech = ("<h3>SEZNAM POJIŠTĚNÝCH</h3>"
          + self._seznam_na_html(seznam, "V evidenci zatím nikdo není"))
          return self._vykresli(obsah_vsech)
