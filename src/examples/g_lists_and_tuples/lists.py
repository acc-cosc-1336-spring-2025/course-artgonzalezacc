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