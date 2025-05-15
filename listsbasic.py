myList = ["pomeranc", "jablko", "kumqat", "meloun"]
print(myList)
print(len(myList))
print(myList[2])
print(myList[int(input("zadejte pozici"))])
dupList = myList [1:3]
print(myList)
print(dupList)

if "jablko" in myList:
    print("Jablko tam je")

myList[-2] = "samice hrabace"
print(myList)

myList.append("grep")
print(myList)

myList.insert(1, "ananas")
print(myList)

myList2 = ["paprika", "mrkev", "okurka"]
myList.extend(myList2)
print(myList)

myList.remove("ananas")
print(myList)

myList.pop(2)

print(myList2)
myList2.clear()
print(myList2)

del myList2

for i in myList:
    print(i)

for i in range(len(myList)):
    print(i, myList[i])

abeceda = ["A", "O", "Y", "D"]
print(abeceda)
abeceda.sort()
print(abeceda)

abeceda.sort(reverse=True)
print(abeceda)

myList.sort()
print(myList)

myList.sort(key=str.lower)
print(myList)

nums=[100,50,65,82,23]
nums.sort()
print(nums)

nums.reverse()
print(nums)

myList2 = myList
print(myList)
print(myList2)

myList2[0] = "rajce"
print(myList)
print(myList2)

copyList = myList.copy()
copyList[0] = "pistacie"
print(myList)
print(copyList)