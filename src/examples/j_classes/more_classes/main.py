from die import Die

def main():
    die = Die()

    for i in range(0, 20):
        print("rolled value: ", die.roll())

main()
