#main program
import value_return_functions


def main():

    for i in range(0, 100):
        result = value_return_functions.get_random_number(1, 100)  
        print(result)  


main()