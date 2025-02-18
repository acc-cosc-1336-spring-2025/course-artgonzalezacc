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
