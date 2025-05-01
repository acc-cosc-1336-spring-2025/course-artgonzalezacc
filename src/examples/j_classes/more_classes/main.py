from die import Die
from roll import Roll

def main():
    die1 = Die()
    die2 = Die()

    for i in range(0, 20):
        roll = Roll(die1, die2)
        print("Roll rolled value: ", roll.roll_value())

main()
