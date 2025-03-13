


cislo1 = int(input("zadejte prvni cislo"))
cislo2 = int(input("zadejte druhy cislo"))

vysledek = cislo1 + cislo2 
print(vysledek)

vysledek = cislo1 * cislo2
print(vysledek)

vysledek = cislo1 - cislo2
print(vysledek)


if cislo2 == 0:
    print("nejde delit")
else: 
    vysledek = cislo1 / cislo2
    print(vysledek)