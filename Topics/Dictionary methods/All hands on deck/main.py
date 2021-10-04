cards_rank = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}

total_points = 0
total_cards = 0

for _ in range(0, 6):
    card = input()
    points = cards_rank[card]
    total_points += points
    total_cards += 1

average_rank = total_points / total_cards
print(average_rank)
