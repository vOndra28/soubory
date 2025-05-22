import random
card = list(range(1, 33))
shuffle = []
n = len(card)
counter = 0
while n > 0:
    i = random.randint(0, len(card)-1)
    counter += 1
    if(card[i] != 0):
        shuffle.append(card[i])
        card[i] = 0
        n -= 1
print(card)
print(shuffle)
print(counter)