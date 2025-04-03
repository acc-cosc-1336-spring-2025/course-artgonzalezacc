def test_config():
    return True

def create_dictionary():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    print(phone_book)

def loop_dictionary_w_for():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    for key in phone_book:
        print(key, phone_book[key])


def dictionary_items():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    for key, value in phone_book.items():
        print(key, value)

def dictionary_keys():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    for key in phone_book.keys():
        print(key, phone_book[key])

def dictionary_values():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    for value in phone_book.values():
        print(value)