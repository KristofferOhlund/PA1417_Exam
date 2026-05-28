import random as rnd

class Game:
    def roll_dice(self):
        number = rnd.randint(1,6)
        if number < 3:
            print("you lose")
            return 0
        else:
            if number == 6:
                print("you win")
                return 2
            else:
                print("Try again")
                return 1