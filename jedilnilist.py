import datetime

#Koncept je, da lastniku naredis meni in mu ponudis moznost dodajanja dni in menije v teh dnevih

dan = {0 : "Ponedeljek", 1 : "Torek", 2 : "Sreda", 3 : "Cetrtek", 4 : "Petek", 5 : "Sobota", 6: "Nedelja"}
#meni je nested dict
meni = {
    'Ponedeljek' : {
        'Goveja juha' : '3e',
        'Makaroni v smetanovi omaki' : '9e',
        'Sladica' : '3e'
    },
    "Torek" : {
        "Gobova juha" : "3e",
        "Zrezek" : "9e",
        "Sladica" : "3e"
    },
    "Sreda" : {
        "Juha" : "3e",
        "Siroki rezanci v paradiznikovi omaki" : "9e",
        "Sladica" : "3e"
    },
    "Cetrtek" : {
        "Zelenjavna juha" : "3e",
        "neka glavna jed" : "9e",
        "Sladica" : "3e"
    },
    "Petek" : {
        "Juha" : "3e",
        "Riba" : "9e",
        "Sladica" : "3e"
    },
    "Sobota" : {
        "Juha" : "3e",
        "Glavna jed" : "9e",
        "Sladica" : "3e"
    },
    "Nedelja" : {
        "Juha" : "3e",
        "Jed" : "9e",
        "Sladica" : "3e"
    }
}
dnevni_meni = meni[dan[datetime.datetime.today().weekday()]]
lastnik = "ne"

#Func za dodajanje v meni zaradi principa DRY
def dodajanje_menija():
    ime_dneva = raw_input("Vnesi dan katerega dodajas: ")
    ime_jedi = raw_input("Vnesi ime jedi: ")
    cena_jedi = raw_input("Vnesi ceno jedi: ")
    meni[ime_dneva] = {ime_jedi: cena_jedi}
    print "Dodal si jedi za " + ime_dneva + ", te jedi so: "
    print meni[ime_dneva]


if lastnik == "ne":
    print "Dobrodosli v restavraciji Prijatelji!"
    print "\t"
    print "Na meniju za " + dan[datetime.datetime.today().weekday()] + " je:"
    for key,value in dnevni_meni.iteritems():
        print (key,value)


print "\t"
#ce ima lastnik zeljo dodati jedi
lastnik = raw_input("Ali ste lastnik restavracije? (da/ne)")

if lastnik == "da":
    dodajanje_menija()
    dodatne_jedi = raw_input("Zelis dodati se vec jedi? (da/ne) ")
    if dodatne_jedi == "da":
        dodajanje_menija()
    else:
        print "Hvala"
else:
    print "Hvala za obisk, nasvidenje"


