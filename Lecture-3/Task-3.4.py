from random import choice

value = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
suit = ["♣", "♦", "♥", "♠"]

print(f"{choice(suit)}{choice(value)}")

