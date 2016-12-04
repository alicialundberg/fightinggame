import random
from characters.character import Character
# Depends on the Player class

class Enemy(Character):
    def __init__(self, strength, defense):
        super(Enemy, self).__init__(100, strength, defense)  # Import the Constructor from superclass Character
        self.strength = strength   # Polymorphism, the subclass overrides the superclass constructor
        self.defense = defense

    def fightplayer(self, other):  # Method to do damage on player
        other.health -= (int(self.strength / random.uniform(1, 1.5) - other.defense))
        print(other.health)

