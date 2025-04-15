#main program
import exceptions

def main():
    num2 = 0
    num1 = 0
    
    while(num2 == 0 ):
        
        num1 = input('Enter a number: ')
        while(not num1.isdigit()):
            num1 = input('Enter a number(1234 etc): ')
        
        num2 = input("Enter divisor(must be gt 0): ")
        while(not num2.isdigit()):
            num2 = input("Enter divisor(must be gt 0) (1234 etc): ")

        num2 = int(num2)

    exceptions.divide_by_zero(int(num1), int(num2))

    exceptions.divide_by_zero(5, 0)

    

main()
