class Celle:
    
    def __init__(self):
        #Default status er død
        self._status = 'Doed'

    def settDoed(self):
        self._status = 'Doed'

    def settLevende(self):
        #Sett celle status til levende
        self._status = 'Levende'

    def erLevende(self):
        #Sjekk hvis celle er levende og returnere True, ellers False
        if self._status == 'Levende':
            return True
        return False
   
    def hentStatusTegn(self):
        #Tegner celle som 'O' hvis det er levende og '.' hvis det er doed
        if self._status == 'Levende':
            return "O"
        return "."
