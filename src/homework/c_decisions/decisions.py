def get_options_ratio(option, total):
    return option / total

def get_faculty_rating(ratio):
    ratio = ratio * 10
    rating = ""
    
    if ratio >= 9 and ratio <= 10:
        rating = "Excellent"
    elif ratio >= 8 and ratio < 9:
        rating = "Very Good"
    elif ratio >= 7 and ratio < 8:
        rating = "Good"
    elif ratio >= 6 and ratio < 7:
        rating = "Needs Improvement"
    elif ratio >= 0 and ratio < 6:
        rating = "Unacceptable"
    else:
        rating = "Invalid ratio"

    return rating
        
        
