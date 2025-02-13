import decisions

def main():
    year = input("Enter a year: ")
    
    result = decisions.get_generation(int(year))
    
    print(result)
    
    

main()

