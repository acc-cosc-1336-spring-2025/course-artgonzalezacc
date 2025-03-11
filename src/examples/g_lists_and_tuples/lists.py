import array

def test_config():
    return True

def use_int_array():
    list_array = array.array('i')

    list_array.append(3)
    print(list_array[0])
    
    list_array.append(1)
    print(list_array[1])

    list_array.append(5)
    print(list_array[2])

def modify_list_array_elements():
    list_array = array.array('i', [3, 1, 5])
    print(list_array[2])

    list_array[1] = 2

    print(list_array[1])