import json
import requests
from random import randint



response = requests.get("https://restcountries.eu/rest/v2/all")
todos = json.loads(response.text)
rand = (randint(1,249))
drzava = todos[rand]["name"]
mesto = todos[rand]["capital"]




def quiz():
    poskusi = 3
    while poskusi > 0:
        odgovor = raw_input("Kaj je glavno mesto drzave " + drzava + "? ")
        if odgovor == mesto:
            print "Cestitke!"
            break
        else:
            poskusi -= 1
            print "Napacno!"
            if poskusi == 0:
                print " "
            else:
                print "Imas se " + str(poskusi) + " poskusov."
    else:
        print "Konec igre, nisi uganil mesta"


quiz()