def get_hamming_distance(dna1, dna2):
    hamming_distance = 0

    if(len(dna1) == len(dna2)):
        for i in range(0, len(dna1)):
            if(dna1[i] != dna2[i]):
                hamming_distance += 1

    return hamming_distance

def get_dna_complement(dna):
    reverse_string = get_reverse_string(dna)
    complement = ''

    for ch in reverse_string:
        if(ch == 'A'):
            complement += 'T'
        elif(ch == 'T'):
            complement += 'A'
        elif(ch == 'C'):
            complement += 'G'
        elif(ch == 'G'):
            complement += 'C'

    return complement

def get_reverse_string(str):
    reverse_string = ''
    index = len(str) - 1

    while(index >= 0):
        reverse_string += str[index]
        index -= 1

    return reverse_string

def display_menu():
    print('1-Get Hamming Distance')
    print('2-Get Reverse Complement')
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
        dna1 = input('Enter dna string A, C, G, T: ')
        dna2 = input('Enter dna string A, C, G, T: ')
        
        hamming_distance = get_hamming_distance(dna1, dna2)

        print("Hamming Distance: ", hamming_distance)
        print('')

    elif(option == '2'):

        dna = input('Enter dna string A, C, G, T: ')        

        complement = get_dna_complement(dna)
        print("Complement: ", complement)
        print('')

    elif(option == '3'):
        print('Program will exit...')
        print('')
