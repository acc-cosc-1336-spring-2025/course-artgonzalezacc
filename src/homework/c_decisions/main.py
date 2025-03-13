import decisions

def main():
    options = int(input('Enter options: '))
    total = int(input('Enter total: '))

    ratio = decisions.get_options_ratio(options, total)

    rating = decisions.get_faculty_rating(ratio)

    print(rating)

main()