def test_config():
    return True

def use_a_while_loop(num):

    counter = 0

    while(counter < num):#boolean expressions while true loops if false stops looping
        #statement that makes the boolean expression false
        print(counter, counter < num,  'Hello')

        counter = counter + 1
        if(counter == 3):
            print(counter, counter < num,  '')

#3   1*1 + 2*2 + 3*3 = 14
#4    1*1 + 2*2 + 3*3 + 4*4 = 30
#5    1*1 + 2*2 + 3*3 + 4*4  + 5*5= 55
def get_sum_of_squares(num): #4
     
    sum = 0

    while(num > 0):
        sum = sum + num * num
        num = num - 1 #will make num > 0 False
         
    return sum

def display_menu():
    print('1-Use a while loop')
    print('2-Sum of squares')
    print('3-Exit')

def run_menu():
    user_option = '0'
    
    while(user_option != '3'):
        
        display_menu()

        user_option = input("Enter a menu option(1,2,3): ")
        handle_menu(user_option)

def handle_menu(user_option):

    if(user_option == '1'):
        num = input("Enter a number: ")
        result = use_a_while_loop(int(num))
        print("Use while loop: ", result)
    elif(user_option == '2'):
        num = input("Enter a number")
        result = get_sum_of_squares(int(num))
        print("Get sum of squares: ", result)
    elif(user_option == '3'):
        print('Exiting...')
    else:
        print("Invalid menu option")

def use_a_for_range_loop(num):
    
    for val in range(0, num):
        print(val, "hello");

#3   1*1 + 2*2 + 3*3 = 14
#4    1*1 + 2*2 + 3*3 + 4*4 = 30
#5    1*1 + 2*2 + 3*3 + 4*4  + 5*5= 55
def get_sum_of_squares_for(num):
    sum = 0

    for n in range(0, num):
        sum += (n+1) * (n+1) #square     sum += is the same as sum = sum + something
    
    return sum

def nested_while_loop(num):
    i = 0

    while(i < num):
        j = 0
        print("Waiting for inner while loop...")

        while(j < num):
            print("\tInner while loop running...")
            j += 1
        
        i += 1

def for_nested_loop(num):

    for i in range(0, num):
        print('Waiting for inner loop...')

        for j in range(0, num):
            print('\tInner loop running...')