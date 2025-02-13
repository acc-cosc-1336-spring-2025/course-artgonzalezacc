def test_config():
    return True

def compare_numbers_equality(num1, num2):
    #num1==num2 is a boolean expression; it returns True/False
    result = num1 == num2; #== means compare ----- = means assign a value to variable
    return result

#  1 10 --->  5
def is_number_in_range(min_range, max_range, num):
    return num >= min_range and num <= max_range

def is_vowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def is_consonant(letter):
    return not(is_vowel(letter))

def is_even(num):
    return num % 2 == 0

def get_generation(year):
    generation = ''

    if year >= 1910 and year <= 1924:
        generation = "The Greatest Generation"
    elif year >= 1925 and year <= 1945:
        generation = "The Silent Generation"
    elif year >= 1946 and year <= 1964:
        generation = "Baby Boomer Generation"
    elif year >= 1965 and year <= 1979:
        generation = "Generation X"
    elif year >= 1980 and year <= 1994:
        generation = "Generation Y"
    elif year >= 1995 and year <= 2012:
        generation = "Generation Z"
    elif year >= 2013 and year <= 2024:
        generation = "Generation Alpha"
    else:
        generation = "Invalid Year"

    return generation

    