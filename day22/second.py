with open("input.txt") as inp:
    raw_decks = inp.read().split("\n\n")
    raw_decks[1] = raw_decks[1][:-1]

starting_decks = [
    list(map(lambda card: int(card), raw_decks[i].split('\n')[1:]))
    for i in range(2)
]
print(starting_decks)
ending_decks = [[], []]
next_game = 1


def recursive_combat(decks: list) -> bool:
    global ending_decks
    global next_game
    game_num = next_game
    print(f'=== Game {game_num} ===')

    previous_configurations = set()
    round_num = 0
    while len(decks[0]) != 0 and len(decks[1]) != 0:
        round_num += 1
        print(f'\n-- Round {round_num} (Game {game_num}) --')
        print(f'Player 1\'s deck: {str(decks[0])[1:-1]}')
        print(f'Player 2\'s deck: {str(decks[1])[1:-1]}')

        if (tuple(decks[0]), tuple(decks[1])) in previous_configurations:
            print('loop prevention')
            return True
        previous_configurations.add((tuple(decks[0]), tuple(decks[1])))

        drawn_cards = (decks[0].pop(0), decks[1].pop(0))
        print(f'Player 1 plays: {drawn_cards[0]}')
        print(f'Player 2 plays: {drawn_cards[1]}')

        if drawn_cards[0] <= len(decks[0]) and drawn_cards[1] <= len(decks[1]):
            next_game += 1
            print('Playing a sub-game to determine the winner...\n')
            p1_wins = recursive_combat([decks[0][:drawn_cards[0]], decks[1][:drawn_cards[1]]])
            print(f'\n...anyway, back to game {game_num}.')
        else:
            p1_wins = drawn_cards[0] > drawn_cards[1]

        if p1_wins:
            print(f'Player 1 wins round {round_num} of game {game_num}!')
            decks[0].extend(drawn_cards)
        else:
            print(f'Player 2 wins round {round_num} of game {game_num}!')
            decks[1].extend(drawn_cards[::-1])
        if game_num == 1:
            ending_decks = decks
    print(f'The winner of game {game_num} is player {1 if decks[0] else 2}!')
    if decks[0]:
        return True


recursive_combat(starting_decks)
winner_score = 0
winner = 0 if ending_decks[0] else 1
for i in range(len(ending_decks[winner]), 0, -1):
    winner_score += i * ending_decks[winner].pop(0)
print(winner_score)
# >>> 35070
