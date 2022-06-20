import random
from random import randint
from celle import Celle

class Spillebrett:
    #Opprette Spillebrett
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = [[Celle() for k in range(self._kolonner)] for r in range(self._rader)]
        self._generasjonsnummer = 0
        #Kaller for _generer metoden som gir en celle 1/3 sjanse å leve/reprodusere 
        self._generer()
    #Skriver ut brettet som fyller opp med celler
    def tegnBrett(self):
        for rad in self._rutenett:
            for kolonne in rad:
                print(kolonne.hentStatusTegn(),end='')
            print()
    #Sortere celler inn to lister og sjekker mengden av naboceller for å bestemme cellens status
    #i følge av reglene
    def oppdatering(self):
        sett_celle_lever = []
        sett_celle_doed = []
        #Oppdatere gjenerasjon nummer hver gang metoden er kallt 
        self._generasjonsnummer += 1
        #Iterere gjennom alle cellene og sortere til korresponde liste
        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                celler = self._rutenett[rad][kolonne]
                celle_lever = celler.erLevende()
                nabo = self.finnNabo(rad,kolonne)

                antall_levende_nabo = 0
                for cell in nabo:
                    if cell.erLevende():
                        antall_levende_nabo += 1

                if celle_lever:
                    if (antall_levende_nabo < 2) or (antall_levende_nabo > 3):
                        sett_celle_doed.append(celler)
                else:
                    if (antall_levende_nabo == 3):
                        sett_celle_lever.append(celler)
        
        for celle in sett_celle_lever:
            celle.settLevende()

        for celle in sett_celle_doed:
            celle.settDoed()

    #Teller antall levende celler i brettet
    def finnAntallLevende(self):
        levende_Celler = 0
        for brett in self._rutenett:
            for celle in brett:
                if celle.erLevende():
                    levende_Celler += 1
        return levende_Celler
    #Lag et ny brett
    def _generer(self):
        for rad in self._rutenett:
            #Sjanse for en celle å leve
            for kolonne in rad:
                if random.randint(0, 2) == 1:
                    kolonne.settLevende()

    
    def finnNabo(self,rad,kolonner):
        Nabo_liste = []
        #Løkken går gjennom -1 og 2 å sjekke riktig rad og kolonne 
        #-1 for å sjekke forrige rad, 0 nåværende rad, 1 - 2 neste rader
        for r in range(-1,2):
            for k in range(-1,2):
                nabo_rad = rad + r
                nabo_kol = kolonner + k
        
                nabo = True
            #Sjekk hvis celler er naboer og ikke selv
                if (nabo_rad) == rad and (nabo_kol) == kolonner:
                    nabo = False

                if (nabo_rad) < 0 or (nabo_rad) >= self._rader:
                    nabo = False
                
                if (nabo_kol) < 0 or (nabo_kol) >= self._kolonner:
                    nabo = False
                
                if nabo:
                    Nabo_liste.append(self._rutenett[nabo_rad][nabo_kol])
        
        return Nabo_liste
    
    #Metod for å returnere generasjons nummer som brukes i main.py
    def hentGenerasjon(self):
        return self._generasjonsnummer
