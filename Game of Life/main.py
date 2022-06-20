from spillebrett import Spillebrett

def main():
    #Hent spillebrett størrelse fra brukeren
    rad_input = int(input('Skriv inn rader: '))
    kolonne_input = int(input('Skriv inn kolonner: '))
    #Opprette spillebrett objekt
    run_game = Spillebrett(rad_input,kolonne_input)
    #Lag første generasjon
    run_game.tegnBrett()
    
    print(f"Generasjon: {run_game.hentGenerasjon()} | Antall levende celler: {run_game.finnAntallLevende()}")
    print('\n')
    #Menyløkke å velge dersom brukeren vil fortsett eller avslutt
    program_status = ''
    while program_status != 'q':
        program_status = input('\nTrykk ENTER for å fortsette. Skriv inn "q" og trykk enter for å avslutte: ').lower()
        #Lag ny generasjon
        if program_status == '':
            run_game.oppdatering()
            run_game.tegnBrett()
            print(f"Generasjon: {run_game.hentGenerasjon()} | Antall levende celler: {run_game.finnAntallLevende()}")
#Kjør program
main()
