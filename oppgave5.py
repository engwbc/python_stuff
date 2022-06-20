#OPPGAVE
#Skriv et enkel quiz som har et poeng system
#Hvis brukeren når en viss poengsum, vinner de quizen og hvis de svarer for mange spørsmål feil, taper de og de kan valge å starte på nytt.

from os import system, name
#Importert å forskinkelse diverse funksjoner med time.sleep()
import time
#For randomisere spørsmålene i quizen 
import random

#Clear-funskjonen er definert som lar programmet fjerne alt som var tryket på skjermen
def clear():
    if name == 'nt':#Hvis OS = Windows, brukes "cls" i terminalen
        _ = system('cls')
    else:
        _ = system('clear')#Hvis OS = Linux/MacOS, brukes "clear" i terminalen

print('Enter your name here:\n')
brukernavn = input()#Jeg var ikke for strenge om innputt her...
time.sleep(0.1)#Meldingen nedenfor er forskinket med 100millisekunder
print(f"Ok, {brukernavn}! Let's get started!")
input("\nAnswer 3 questions and win. Try not to get below -2 points or it's game over.\n"
      "Press any ENTER to continue\n")
clear()

#class lagres et objekt "Question" som innholder et spørsmål (prompt) og svar(answer)
class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

#Liste av spørsmål med valg
questionslist = [
    "What is the capital city of Norway?\n(a) Oslo\n(b) Trondheim\n(c) Fredrikstad\n(d) Bergen",
    "Who is the current prime minister of England?\n(a) Theresa May\n(b) Boris Johnson\n(c) Margaret Thatcher\n(d) David Cameron",
    "What is the square root of 169?\n(a) 13\n(b) 14\n(c) 15\n(d) 16",
    "Is water a polar molecule?\n(a) Yes\n(b) No",
    "When did the Great Depression start?\n(a) 1942\n(b) 1899\n(c) 1925\n(d) 1929",
    "What electromagnetic radiation has the shortest wavelength?\n(a) X-ray\n(b) Gamma ray\n(c) UV\n (d)Microwave",
]
#Dette variabel "Question" skal programmet ta spørsmålene ovenfra og oppgi det riktig svaret
questions = [Question(questionslist[0], "a"), Question(questionslist[1], "b"), Question(questionslist[2], "a"),
            Question(questionslist[3],"a"), Question(questionslist[4],"d"), Question(questionslist[5],"b")]
#Randomisere spørsmål
random.shuffle(questions)
#gametime-funskjonen lar programmet starte quizen
def gametime(questions):
    poeng = 0 #Poeng variabel
    for question in questions:
        print(question.prompt)
        svar = input("Answer: ")
        if svar == question.answer:
            poeng += 1 #Et poeng er lagt til for hvert riktig svar
            print(f"Correct. Point get! Current points: {poeng}\n")
            time.sleep(0.5)
            if poeng == 3:
                print(f"Congratulations {brukernavn}, you beat the quiz!")#Hurrah!
                break
        else:
            poeng -= 1 #Brukeren mister et poeng for hvert feil svar
            time.sleep(0.5)
            print(f"Incorrect! Point lost. Current points: {poeng}\n")
            if poeng <= -3:
                return provigjen() #Hvis poengsummen er -3, programmet kalles for provigjen-funksjonen å starte på nytt. Prøv igjen!
#'Restart' funksjon           
def provigjen():
    while True:
        gjenta = input("You have chosen too many incorrect answers! Try again?\n[YES] [NO]\n").casefold()
        if gjenta not in {'y','yes','n','no'}:
            print("Please answer yes or no") #Sjekker om input er som det er oppført ovenfor
        elif gjenta == "y" or "yes":
            clear()
            return gametime(questions) #Hvis brukeren svaret ja, programmet returnerer til starte
        elif gjenta == "n" or "no":
            sys.exit() #Slutter program
        
#Quizen kjøres
gametime(questions)

