class Customer:
    __customer_id = 0
    __first_name = ''
    __last_name = ''

    def __init__(self, id, first_name, last_name):
        self.__customer_id = id
        self.__first_name = first_name
        self.__last_name = last_name
    
    def get_customer_id(self):
        return self.__customer_id
    
    def get_customer_name(self):
        return self.__first_name + ' ' + self.__last_name
