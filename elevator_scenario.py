
#Variable defining the current floor
aktuelle_Etasje = int(0) #Use int as we don't really have half of a floor (we assume the building doesn't have a mezzanine!)

def heisProgram():
    valgt_Etasje = int(input("Select a floor: "))
    print("\nGoing up!")
    if valgt_Etasje > 13: #If the selected floor is greater than 13, the program subtracts by 1 to give the actual floor.
        aktuelle_Etasje = valgt_Etasje - 1
        print("Floor:",aktuelle_Etasje)
    else: #When floor is lower than 13, the program keeps the given floor 
        aktuelle_Etasje = valgt_Etasje
        print("Floor:",aktuelle_Etasje)


heisProgram()
