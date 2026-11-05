from evidence import Evidence
from rozhrani_views import Rozhrani

# tenhle soubor vše spustí na jednom místě  = spouštěcí

evidence = Evidence()  # udělej evidenci dle evidence.py
rozhrani = Rozhrani(evidence)  # vezme evidenci a dá jí do rozhraní

rozhrani.spust()  # tady se prostě spustí

