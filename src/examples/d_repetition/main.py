import repetition


def main():
    num = input("Enter a number: ")#captured from keyboard as a string
    
    result = repetition.get_sum_of_squares(int(num)) #int means convert num to a number
    
    print(result)

#run the main function
main()

