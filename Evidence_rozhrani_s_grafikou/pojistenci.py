class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon, id=None):
        self.id = id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon


    def to_dict(self):          # převod objektu na slovník
        return {
            "id":self.id,
            "jmeno":self.jmeno,
            "prijmeni":self.prijmeni,
            "vek":self.vek,
            "telefon":self.telefon,
    }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["jmeno"],
            data["prijmeni"],
            data["vek"],
            data["telefon"],
            data.get("id"),
        )

    def __str__(self):
        return f"Jméno: {self.jmeno}, Přijmení: {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"
