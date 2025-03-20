import random
krok = 0

while True:
    krok += 1
    kostka1 = random.randint(1, 6)
    kostka2 = random.randint(1, 6)



    print(str(kostka1) + " " + str(kostka2))
    if kostka1 == kostka2:
        break
print("pocet hodu nutnych k uspechu byl: " + str(krok))