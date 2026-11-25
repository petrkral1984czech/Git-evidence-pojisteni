from evidence import Evidence
from rozhrani import Rozhrani

evidence = Evidence()   # spustí běh evidence programu, kde se načte i soubor json...
rozhrani = Rozhrani(evidence)  # tady předám do rozhrani __init__ data objektu evidence a uloží v rozhraní __init__ self. evidence...

rozhrani.app.run(debug=True)