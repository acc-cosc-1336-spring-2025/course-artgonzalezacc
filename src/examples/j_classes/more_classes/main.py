from src.examples.j_classes.more_classes.player import Player
from src.examples.j_classes.more_classes.die import Die

def main():
    die1 = Die()
    die2 = Die()

    player = Player()
    player.roll_dice(die1, die2)
    player.roll_dice(die1, die2)
    player.roll_dice(die1, die2)
    player.roll_dice(die1, die2)
    player.roll_dice(die1, die2)
    player.roll_dice(die1, die2)

    rollList = player.get_rolls()

    for roll in rollList:
        print(roll.roll_value())
    

main()
