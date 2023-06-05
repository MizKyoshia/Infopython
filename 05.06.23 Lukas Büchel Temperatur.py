#Programm für Temperaturen
#Autor: Lukas Büchel
#Datum: 05.06.23

temp = []

while True:
    tempinput = str(input("Gib eine beliebige Temperatur ein oder ende zum beenden! ")) #allgemeiner Input
    if tempinput == "ende":
        print("Die Eingabe wurde beendet!")
        break
    temp.append(float(tempinput)) #Eingabe der Temperaturen vom Nutzer  
    tempmw = float(sum(temp) / len(temp)) #Durchschnittliche Temperatur, Berechnung mit sum() & len()
    print("Die durchschnittliche Temperatur aus "+str(temp)+" beträgt "+str(tempmw)) #finale Ausgabe