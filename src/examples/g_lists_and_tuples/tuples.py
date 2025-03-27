#
def create_a_tuple():
    tuple = (1, 2, 3, 4, 5) # read only list
    print(tuple[0])

def loop_a_tuple():
    tuple = (1, 2, 3, 4, 5) # read only list

    for item in tuple:
        print(item)

    print('------------------')

    for i in range(0, len(tuple)):
        print(tuple[i])

    print('-----------------')

    indx = 0

    while(indx < len(tuple)):
        print(tuple[indx])
        indx += 1

def convert_tuple_to_list():
    tuple = (4, 1, 9)
    list1 = list(tuple) #convert tuple to a list

    print(list1)

def convert_list_to_tuple():
    list1 = [8, 1, 0]
    tuple1 = tuple(list1)

    print(tuple1)


