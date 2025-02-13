print("zadejte prvni cislo")
x = int(input())
print("zadejte druhy cislo")
y = int(input())
if x > y:
    print(str(x) + " je vetsi nez " + str(y))
elif x==y:
      print("Cisla jsou stejna")
else:
        print(str(x) + " je mensi nez " + str(y))