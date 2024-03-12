
n = int(input())

cards =list(range(1,n+1))

while len(cards) != 1:
    if len(cards) % 2 == 0:
        cards = cards[1::2]
    else:
        cards = cards[1::2]
        cards = cards[1:]+[cards[0]]

print(cards.pop())