import random

izbran_level = raw_input("Izberi stopnjo igre pri tem, da je 1 najlazja in 10 najtezja: ")
level_dict = { 1:[1,10],
               2:[1,20],
               3:[1,30],
               4:[1,40],
               5:[1,50],
               6:[1,60],
               7:[1,70],
               8:[1,80],
               9:[1,90],
               10:[1,100],
}
level = level_dict[int(izbran_level)]

def main(level):
    prva = level[0]
    druga = level[1]
    skrita_stevilka = random.randint(prva,druga)


    while True:
        odgovor = int(raw_input("Ugani stevilko med %s in %s: " %(str(prva), str(druga))))

        if odgovor == skrita_stevilka:
            print "Cestitke! %s je skrita stevilka" %skrita_stevilka
            break
        elif odgovor > skrita_stevilka:
            print "Poskusi znova, stevilka je previsoka"
        elif odgovor < skrita_stevilka:
            print "Poskusi znova, stevilka je prenizka"


if __name__ == "__main__":
    main(level)
