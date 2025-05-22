import random
card = list(range(1, 33))
shuffle = []
n = len(card)
counter = 0

while n:
    n -= 1    
    i = random.randint(0,n)
    shuffle.append(card.pop(i))
    print(card)
    print(shuffle)
    counter +=1
print(counter)