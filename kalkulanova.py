while True:
    clen1 = int(input("Zadej cislo"))
    clen2 = int(input("Zadejte cislo"))
    
    """
    print("1. soucet")
    print("2. soucin")
    print("3. rozdil")
    print("4. podil")
    """
    print("1. soucet \n2. soucin\n3. rozdil\n4. podil")

    operace = int(input("Vyberte cislo pocetni operace, kterou chcete?"))
        
    match operace:
        case 1:
            soucet = clen1 + clen2
            print("soucet je" + str(soucet))
        case 2:
            soucin = clen1 * clen2
            print("ssoucin je" + str(soucin))
        case 3:
            rozdil = clen1 - clen2
            print("podil je" + str(rozdil))
   
        case 4:
            if clen2 == 0:
                print("nejde delit 0")
            else:
                podil = clen1 / clen2
                print("podil je" + str(podil))
    

    
    konec = input("Prejete si ukoncit program? Y/N")
    if konec == "Y" or konec == "y":
        break
    elif konec == "N" or konec == "n":
        print("Jedeme dál")
    else:
        print("neplatne zadani")
        break