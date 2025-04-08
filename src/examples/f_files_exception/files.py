#
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

