def test_config():
    return True

def display_menu():
    print('1-Enter Survey Responses')
    print('2-Get Survey Results')
    print('3-Exit')

def run_menu():
    option = 0

    while option != 3:
        display_menu();
        option = int(input('Enter option: '))
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == 1):
        print('display survey question')
    elif(option == 2):
        print('survey results')
    elif(option == 3):
        print('Exiting...')
    else:
        print('Invalid option ...')
