import time

from characters.player import Player
from characters.enemy import Enemy

#  Initiating the variables
player1 = Player(75, 40)
fighter1 = Enemy(80, 35)
fighter2 = Enemy(90, 40)



def play():
    startgame = input("Start Game? (y/n) ")
    #  While loop to start the game
    while startgame != "Y" not in "N":
        name = input("Enter Name: ")
        print("Welcome to the MMA - Fighting game!\n")

        def firstbattle():
            print("In the Red corner, we have a powerful fighter named " + name)
            time.sleep(1)
            print("In the Blue corner, we have the 3rd best in this weightclass!\n")
            time.sleep(2)
            print("LEEET\'S GET REEEADY TO RUUUUMBLEEEE! \n")
            time.sleep(1)

            while player1.health > 0 and fighter1.health > 0:

                player1.fightenemy(fighter1)
                if fighter1.health <= 0:
                    break
                elif player1.health <= 0:
                    print("Your health is too low. \nGame over.")
                    break
                else:
                    time.sleep(1)
                    print("\nThe fighter attacked you back! \nYour health is now: ")
                    fighter1.fightplayer(player1)
                    print(" ")
        firstbattle()

        def gethealth():
            power = input("Oh no, your health is getting low! Do you want to increase your health? (Y/N)")
            if power.upper() == "Y":
                    player1.health += 80
                    player1.strength += 10
            else:
                print("Well, it\'s your choice....")
        gethealth()

        print("After the last battle, you will meet harder competition.\n")
        player1.checkHealth()
        time.sleep(1)
        print("\n Loading....\n")
        time.sleep(2.5)

        def secondbattle():
            print("In the Red corner, we have a powerful fighter named " + name)
            time.sleep(1)
            print("In the Blue corner, we have the 2nd best in this weightclass!\n")
            time.sleep(2)
            print("LEEET\'S GET REEEADY TO RUUUUMBLEEEE! \n")
            time.sleep(1)

            while player1.health > 0 and fighter2.health > 0:

                player1.fightenemy(fighter2)
                if fighter2.health <= 0:
                    break
                else:
                    print("The enemy attacked you back! \nYour health is now: ")
                    fighter2.fightplayer(player1)

        secondbattle()
play()

# The game is not finished yet!
