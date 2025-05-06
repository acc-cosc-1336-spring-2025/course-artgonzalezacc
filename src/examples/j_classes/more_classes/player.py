from src.examples.j_classes.more_classes.roll import Roll

class Player: 
    def roll_dice(self, die1, die2):
        roll = Roll(die1, die2)

        return roll
