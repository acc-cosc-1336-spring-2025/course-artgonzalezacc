from src.examples.j_classes.more_classes.roll import Roll

class Player: 
    __roll_list = []
    
    def roll_dice(self, die1, die2):
        roll = Roll(die1, die2)
        self.__roll_list.append(roll)

        return roll
    
    def get_rolls(self):
        return self.__roll_list
