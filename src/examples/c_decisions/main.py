import decisions

def main():
    num1 = input("Enter number: ")
    num2 = input("Enter number: ")
    
    result = decisions.compare_numbers_equality(int(num1), int(num2))

    print(result)

main()

