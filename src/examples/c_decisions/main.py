import decisions

def main():
    num = input("Enter a number: ")
    
    result = decisions.is_even(int(num))
    
    print(result)
    
    if(result):
        print(num, " is even")
    else:
        print(num, "is odd")
    

main()

