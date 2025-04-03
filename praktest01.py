print("S jakym tvarem si prejete pracovat? ctverec, obdelnik nebo trojuhelnik")
tvar = input()

if tvar == "ctverec":
    print("Zadejte delku strany (a):")
    strana = int(input())
    print("obvod nebo obsah")
    tip = input()

    if tip == "obsah":
        obsah = strana * strana
        print(obsah)
    elif tip == "obvod":
        obvod = 4 * strana
        print(obvod)
    else:
        print("neplatna volba")

elif tvar == "obdelnik":
    print("Zadejte délku strany (a, b):")
    a = int(input())
    b = int(input())
    print("obvod nebo obsah")
    tip = input()

    if tip == "obsah":
        obsah = a * b
        print(obsah)
    elif tip == "obvod":
        obvod = 2 * (a + b)
        print(obvod)
    else:
        print("neplatna volba")
else:
    tvar == "trojuhelnik"
    print("zadejte delku strany (a, b, c)")
    a = int(input())
    b = int(input())
    c = int(input())
    
    if a == b == c:
        int((a + b) > c)
        int((b + c) > a) 
        int((a + c) > b)
        print("lze udelat trojuhelnik")
    else:
        print("nelze sestavit")