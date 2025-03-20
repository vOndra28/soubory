end = int(input("Zadejte cislo jehoz faktorial chcete"))
faktorial = 1

for  i in range(1, end + 1): 
    faktorial *= i
    print(faktorial)
print(faktorial)