while True:
    cislo = input("zadejte cislo: ")
    if cislo.isdigit():
        max = int(cislo)
        break



while input("Pro ukončení zadejte pismeno K") != "K" :
    cislo = input("Zadejte cislo")
    if cislo.isdigit():
        cislo = int(cislo)
        if max < cislo:
            max = cislo
    
print("Nejvetsi cislo blyo: " + max)