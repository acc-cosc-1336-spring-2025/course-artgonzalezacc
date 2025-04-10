#
import pickle

def write_to_file(file_name):
    file = open(file_name, 'w') #open a text file for writing

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()

def read_from_file(file_name):
    file = open(file_name, 'r')

    file_lines = file.read()
    file.close()

    print(file_lines)

def read_from_file_one_line_at_a_time(file_name):
    file = open(file_name, 'r')

    line1 = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')
    line3 = file.readline().rstrip('\n')
    file.close()

    print(line1)
    print(line2)
    print(line3)

def read_from_file_w_while_loop(file_name):
    file = open(file_name, 'r')

    line = file.readline().rstrip('\n')
    while(line != ''):
        print(line)
        line = file.readline().rstrip('\n')

    file.close()

def read_from_file_w_for(file_name):
    file = open(file_name, 'r')

    for line in file:
        print(line.rstrip('\n'))

    file.close()

def write_employee_records(file_name):
    file = open(file_name, 'w')

    choice = '1'

    while choice == '1':
        id = input('Enter id: ')
        name = input('Enter name: ')
        dept = input('Enter dept: ')

        file.write(id + '\t')
        file.write(name + '\t')
        file.write(dept + '\n')

        choice = input('Enter 1 to continue: ')
    
    file.close()

def read_employee_records(file_name):
    file = open(file_name, 'r')

    for employee in file:
        record = employee.split('\t') #this creates a list ['1336', 'Python', 'COSC']

        id = record[0]
        name = record[1]
        dept = record[2].rstrip('\n')

        print(id, name, dept)

    file.close()

def write_prog_lang_list_of_lists(file_name):
    file = open(file_name, 'w')

    prog_langs = [['1980', 'C++', 'Complex'], ['1996', 'Python', 'Easy'], ['1991', 'Java', 'Medium']]

    for lang in prog_langs:
        file.write(lang[0] + '\t')#year
        file.write(lang[1] + '\t')#lang
        file.write(lang[2] + '\n')
    
    file.close()

def read_prog_lang_list_of_lists(file_name):
    file = open(file_name, 'r')

    list_langs = []

    for line in file:
        record = line.split('\t')
        year = record[0]
        lang = record[1]
        level = record[2].rstrip('\n')

        lang_list = [year, lang, level]

        list_langs.append(lang_list)

    print(list_langs)

    for lang in list_langs:
        print(lang[0], lang[1], lang[2])

    file.close()

def write_dictionary_records(file_name):

    prog_langs = {'1' : ['1979', 'C++', 'Bjarne'], '2': ['1991', 'Java', 'Gosling'], '3': ['1996', 'Python', 'Guido']}

    with open(file_name, 'w') as file:
        for key, value in prog_langs.items():
             record_list = value
             file.write(key + '\t') #record identifier
             file.write(record_list[0] + '\t')#year
             file.write(record_list[1] + '\t')#language
             file.write(record_list[2] + '\n')#creator

def read_dictionary_records(file_name):
    
    prog_langs = {}

    with open(file_name, 'r') as file:
        for line in file:
            record = line.split('\t')
            key = record[0]
            year = record[1]
            lang = record[2]
            creator = record[3].rstrip('\n')

            prog_langs[key] = [year, lang, creator]
    
    print(prog_langs)

def pickle_dictionary(file_name):

    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    with open(file_name, 'wb') as file: 
        pickle.dump(phone_book, file)

def unpickle_dictionary(file_name):

    with open(file_name, 'rb') as file:
        phone_book = pickle.load(file)

    print(phone_book)

def read_image_jpg_file(file_name):
    
    with open(file_name, 'rb') as image_file:
        contents = image_file.read()

    print(contents)

