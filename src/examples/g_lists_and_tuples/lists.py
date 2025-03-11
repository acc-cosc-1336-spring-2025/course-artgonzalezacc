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

def use_float_array():
    float_array = array.array('f')
    float_array.append(3.5)
    float_array.append(9.1)
    float_array.append(77.6)
    
    size = len(float_array)

    for i in range(0, size):
        print(float_array[i])

    float_array[2] = 7.6
    print('')
    for i in range(0, size):
        print(float_array[i])

