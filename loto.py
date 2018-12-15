#-*- coding: utf-8 -*-
import random


print "Dobrodosli v Loto Generator aplikaciji"

try:
    najmanjse_str = raw_input("Katero naj bo NAJMANJSE stevilo: ")
    najvecje_str = raw_input("katero naj bo NAJVECJE stevilo: ")
    kolicina_str = raw_input("Prosim vnesite koliko nakljucnih stevilk bi zeleli vnesti: ")

    najmanjse = int(najmanjse_str)
    najvecje = int(najvecje_str)
    kolicina = int(kolicina_str)

    loto_list = list(range(najmanjse, najvecje + 1))

    if najmanjse > najvecje:
        print "Najmanjše število ne mora biti večje od največjega števila.\nPoskusi znova."
    elif kolicina > najvecje:
        print "Količina ne mora biti večja od največjega števila.\nPoskusi znova."
    else:
        output = random.sample(loto_list, kolicina)
        print "Vase loto številke so: %s" % output

except ValueError:
    print "Vnešeni podatki niso številke!"



