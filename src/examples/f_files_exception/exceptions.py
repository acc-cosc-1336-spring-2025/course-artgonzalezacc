def test_config():
    return True

def divide_by_zero(num1, num2):
    if(num2 == 0):
        print("Num2 must be gt 0")    
    else:
        print(str(num1/num2))

def open_a_file_error(file_name):
    
    log_file = open('system_log.dat', 'w')

    try:
        file = open(file_name, 'r')
        
        for line in file:
            amount = int(line)
            print(amount)

        file.close()
    except IOError as err:
        print('Cannot open file: ' + file_name)
        log_file.write("exceptions.py in open_a_file_error: " + str(err) + '\n')
    except ValueError as err:
        print('Invalid numeric data')
        log_file.write("exceptions.py in open_a_file_error: " + str(err) + '\n')
    except:
        print('unknown error')

    log_file.close()

def open_file_read_except_else(file_name):
    try:
        file = open(file_name, 'r')
        
    except IOError:
        print('Cannot read file: ')
    else:
        contents = file.read()
        print(contents)
        file.close()

def open_file_except_finally(file_name):
    try:
        file = open(file_name, 'r')
        #contents = file.read()

        for line in file:
            amount = int(line)
            print(amount)

        #print(contents)
    except IOError:
        print('Cannot open file')
    except ValueError as err:
        print('Invalid numeric data')
    finally: #will always run error or no error
        #close db connections, files, or network connections
        print('Finally always runs')

        if 'file' in locals():
            file.close()