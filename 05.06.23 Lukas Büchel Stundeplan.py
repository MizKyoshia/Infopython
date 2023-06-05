#Programm für Stundenplan
#Autor: Lukas Büchel
#Datum: 05.06.23

tage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
stundenplan = [
    ["1","2","3","4","5","6","7","8"],
    ["Deutsch","Deutsch","Biologie","Biologie","Kunst","Kunst","Informatik"],
    ["Geografie","Geografie","Mathe","Mathe","Geschichte","Geschichte"],
    ["Englisch","Englisch","Wirtschaft/Recht","Wirtschaft/Recht","Französisch","Französisch"],
    ["Informatik","Informatik","Mathe","Deutsch","Musik","Musik"],
    ["Mathe","Deutsch","Englisch","Englisch","Sport","Sport"],
]
def liststundenplan():
    for z in range(len(tage)): #Bestimmung des Tages
        print("Stundenplan für Tag: "+ tage[z]) #Ausgabe des Tages
        for i in range(len(stundenplan[z])): #Bestimmung des Faches des jeweiligen Tages
            print("Std "+stundenplan[0][i]+ ": "+ stundenplan[z][i],) #Ausgabe der jeweiligen Stunde und des Faches

def stundenplan_aendern():
    print("Formular für Veränderung des Stundenplan. Befolge die Anweisungen!")
    tag = input("Gib den Wochentag ein: ")
    stunde = input("Gib die Stunde ein: ")
    fach = input("Gib das neue Fach ein: ")

    tag_index = tage.index(tag)
    stunde_index = stundenplan[0].index(stunde)

    stundenplan[tag_index][stunde_index] = fach
    print("Erfolgreiche Aktualisierung des Stundenplans!")
    liststundenplan()

liststundenplan()
stundenplan_aendern()
liststundenplan()