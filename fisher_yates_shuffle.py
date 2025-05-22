import random
card = list(range(1, 33))
n = len(card)
counter = 0

while n > 1:
    n -= 1
    i = random.randint(0, n- 1)
    card[i], card[n] = card[n], card[i]
    print(i, n, sep="| |")
    print(card)
    counter += 1
print(counter)