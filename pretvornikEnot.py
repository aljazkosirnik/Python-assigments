
#1 kilometer = 0.621371192 miles

nadaljuj = "da"

print("Tukaj lahko izbiras pretvorbo iz km v mi ali pa obratno")
while nadaljuj == "da":
    odlocitev = raw_input("Kaj zelis pretvoriti (1)KM v MI ali (2) MI v KM?:")

    if odlocitev == "1":
        km_to_mi = int(raw_input("Vpisi kilometre: "))
        rezultat_km_to_mi = km_to_mi * 0.621371192
        print(str(km_to_mi) + " kilometrov je " + str(rezultat_km_to_mi) + " milj.")
        nadaljuj = raw_input("Ali zelis nadeljevati? (da, ne) ")

    if odlocitev == "2":
        mi_to_km = int(raw_input("Vpisi milje: "))
        rezultat_mi_to_km = mi_to_km * 1.609344
        print(str(mi_to_km) + " milj je " + str(rezultat_mi_to_km) + " kilometrov.")
        nadaljuj = raw_input("Ali zelis nadeljevati? (da, ne) ")

