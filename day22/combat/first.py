import queue

with open("input.txt") as inp:
    raw_decks = inp.read().split("\n\n")
    raw_decks[1] = raw_decks[1][:-1]

deck_size = 0
decks = [queue.SimpleQueue(), queue.SimpleQueue()]
for i in range(2):
    for card in raw_decks[i].split('\n')[1:]:
        deck_size += 1
        decks[i].put(int(card))

round_num = 0
while True:
    # it doesn't work with this condition in the while statement but this works i guess
    if decks[0].empty() or decks[1].empty():
        break
    played_cards = [decks[0].get(), decks[1].get()]
    round_num += 1
    print(f'\n-- Round {round_num} --')
    print(f'Player 1 plays: {played_cards[0]}')
    print(f'Player 2 plays: {played_cards[1]}')
    if played_cards[0] > played_cards[1]:
        print('Player 1 wins the round!')
        decks[0].put(played_cards[0])
        decks[0].put(played_cards[1])
    else:
        print('Player 2 wins the round!')
        decks[1].put(played_cards[1])
        decks[1].put(played_cards[0])

winner = 1 if decks[0].empty() else 0
winner_score = 0
for i in range(deck_size, 0, -1):
    winner_score += i * decks[winner].get()
print(winner_score)
# >>> 33772
