def get_factorial(num):
    factorial = 1

    for i in range(0, num):
        factorial *= i + 1
    
    return factorial

def sum_odd_numbers(num):
    index = 1
    sum = 0

    while(index <= num):
        sum += index
        index += 2

    return sum

def display_menu():
    print('1-Factorial')
    print('2-Sum Odd Numbers')
    print('3-Exit')

def run_menu():
    choice = 0
    yes_no_choice = ''

    while(choice != '0'):
        display_menu()
        choice = input('Enter menu option: ')

        handle_menu_option(choice)

        if(choice == '3'):
            yes_no_choice = input('Exit Y or N: ')

        if(yes_no_choice == 'y' or yes_no_choice == 'Y'):
            choice = '0'

def handle_menu_option(option):
    if(option == '1'):
        num = 0
        
        while(num < 1 or num > 9):
            num = int(input('Enter a number between 1 to 9: '))

        factorial = get_factorial(num)
        print("Factorial: ", factorial)
        print('')

    elif(option == '2'):

        num = 0

        while(num < 1 or num > 99):
            num = int(input('Enter a number between 1 to 99: '))

        result = sum_odd_numbers(num)
        print("Sum odd numbers: ", result)
        print('')

    elif(option == '3'):
        print('Program will exit...')
        print('')
