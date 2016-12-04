from characters.character import Character
import random
# Depends on the Enemy class

class Player(Character):
    def __init__(self, strength, defense):
        super(Player, self).__init__(100, strength, defense) # Import the Constructor from superclass Character
        self.strength = strength  # Polymorphism, the subclass overrides the superclass constructor
        self.defense = defense

    def fightenemy(self, other):  # Method to do damage on Enemy
        attack = input("Pick a move! A = Punch. B = Bitchslap. C = Kick. ")
        # Iteration structure for the different attacks
        if attack.upper() in 'A':
            print("Good punch! Your enemy\'s health is now: ")
            other.health -= (int(self.strength / random.uniform(1, 1.7) - other.defense))
            print(other.health)
        elif attack.upper() in 'B':
            print("A slap in the face! Your enemy\'s health is now: ")
            other.health -= (int(self.strength / random.uniform(1, 2) - other.defense))
            print(other.health)
        elif attack.upper() in 'C':
            print("Ouch, that kick did some damage! Your enemy\'s health is now: ")
            other.health -= (int(self.strength / random.uniform(1, 1.5) - other.defense))
            print(other.health)
        else:
            print("You hesitate...")

    def checkHealth(self):
        if self.health <= 0:
            print("Your health level is too low. \n Game Over.")
        else:
            print("Your health level is " + str(self.health))
            print("Your strength level is " + str(self.strength))

