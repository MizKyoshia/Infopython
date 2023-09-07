#Programm für ein Quizspiel
#Autoren: Lukas B. Arthur S., Lucio S.
#Fertigstellung am 08.09.2023

import random
score = 0
rangliste = []

#Fragenkatalog

Hardware = [
    {
        "frage": """Was ist die Hauptfunktion einer CPU? 
        a) Grafikverarbeitung b) Datenepeicherung c) Ausführung von Befehlen""",
        "antwort": "c"
    }, {
        "frage": """Welche Art von Hardware speichert dauerhaft Daten, selbst wenn der Computer ausgeschaltet ist?
        a) RAM b) CPU c) Festplatte""",
        "antwort": "c"
    }, {
        "frage": """Welche Hardware-Komponente ist verantwortlich für die drahtlose Verbindung eines Computers mit dem Internet?
        a) GPU b) Router c) Maus""",
        "antwort": "b"
    }, {
        "frage": """Welche Art von Hardware ermöglicht die Eingabe von Informationen in einen Computer durch Berühren oder Bewegen?
        a) Monitor b) Tastatur c) Touchscreen""",
        "antwort": "c"
    }, {
        "frage": """Welche Hardware-Komponente zeigt Informationen visuell auf einem Bildschirm an?
        a) Festplatte b) GPU (Grafikarte) c) Prozessor""",
        "antwort": "b"
    }
]

Gaming = []
Musik = []

#Auswahl 
def fragenAuswahl(fragenKatalog):
    global score
    frage = random.choice(fragenKatalog)
    print(frage["frage"])
    antwort = input("Antwort: ")

    if antwort == frage["antwort"]:
        print("Richtige Antwort!")
        score +=1
    else:
        print(f"Du liegst leider falsch.Die richtige Antwort wäre '{frage[antwort]}'gewesen!")

#Ranglistenanzeige
def zeigeRangliste():
    print("Rangliste:")
    for eintrag in rangliste:
        print(f"{eintrag['name']} - Punktestand: {eintrag['punkte']}")
    print()

#Hauptschleife
def main():
    global score
    print("Herzlich Willkommen zu unseren Quizspiel!")

    spielername = input("Gib deinen Namen ein, um dich zur Rangliste hinzuzufügen: ")
    rangliste.append({"name": spielername, "punkte": 0})

    while True:
        print("""Bitte wähle aus einem Fragenkatalog aus:
              1) Hardware
              2) Gaming
              3) Musik
              """)
        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            print("Viel Spaß beim Fragenkatalog zur Hardware!")
            for i in range(5):
                fragenAuswahl(Hardware)
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score
                    break
            zeigeRangliste()
            score = 0
        elif auswahl == "2":
            print("Viel Spaß beim Fragenkatalog zum Gaming!")
            for i in range(5):
                fragenAuswahl(Gaming)
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score
                    break
            zeigeRangliste()
            score = 0
        elif auswahl == "3":
            print("Viel Spaß beim Fragenkatalog zur Musik")
            for i in range(5):
                fragenAuswahl(Musik)
            print(f"Das Spiel ist beendet! Dein Punktestand liegt bei {score}")
            for eintrag in rangliste:
                if eintrag["name"] == spielername:
                    eintrag["punkte"] = score
                    break
            zeigeRangliste()
            score = 0
            
        elif auswahl == "4":
            print("""Das Spiel wird nun beendet!
                  Vielen Dank fürs Spielen!""")
            zeigeRangliste()
            break
        else:
            print("Bitte gib eine richtige Ziffer ein!")

main()