import decisions

def main():
    num1 = input("Enter min range: ")
    num2 = input("Enter max range: ")
    num3 = input("Enter number: ")
    
    result = decisions.is_number_in_range(int(num1), int(num2), int(num3))

    print(result)

main()

