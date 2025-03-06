def test_config():
    return True

def string_params(str1):
    print(str1)
    str1 = "C++"

def string_return_value(lang):
    lang = "C++"
    print(id(lang))
    return lang

def string_loop_w_while(str):

    index = 0 #0 1 2 3 4 5
    length = len(str) #python has 6 length

    while(index < length):
        print(str[index], index, length)
        index +=1
        if(index == 6):
            print("", index, length)

def string_loop_w_for_range(str):

    length = len(str)

    for index in range(0, length):
        print(str[index], index, length)

def string_loop_w_for(str):

    for ch in str: #Python
        print(ch)
        ch = 'a'#doesn't change str; only changes the ch variable
        
    print(str)

#The password must be at least seven characters long.

#It must contain at least one uppercase letter.

#It must contain at least one lowercase letter.

#It must contain at least one numeric digit
def validate_password(password):
    correct_length = 7
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    if(len(password) >= 7):
        correct_length = True

        for ch in password:
            if ch.upper():
               has_uppercase = True
            if ch.islower():
               has_lowercase = True
            if ch.isdigit():
               has_digit = True

        if correct_length and has_uppercase and has_lowercase and has_digit:
           is_valid = True
        else:
           is_valid = False

        return is_valid
            
            


        




