from customer import Customer


def test_config():
    return True

#Create dictionaries
survey_questions = \
{
    '2.1': 'The texts, assigned readings, and other course resources help me learn the course material.',
    '2.2': 'Clear instructions are provided',
    '2.3': 'Tests, papers, assignments, and or other activities include clear instructions.',
    '2.4': 'Uses instructional technology',
    '2.5': 'Tests, papers, assignments, or other activities'
}

survey_question_options = \
{
    1: 'Never',
    2: 'Sometimes',
    3: 'More',
    4: 'More more',
    5: 'Always',
    6: 'Always Always'
}

#list of lists
survey_responses_list = []#survey_id, option_id, resonse

survey_response_results = {}
survey_response_results_total = {'2.1': 0, '2.2': 0, '2.3': 0, '2.4': 0, '2.5': 0}

def display_menu():
    print('1-Enter Survey Responses')
    print('2-Get Survey Results')
    print('3-Exit')

def run_menu():
    option = 0

    while option != 3:
        display_menu();
        option = int(input('Enter option: '))
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == 1):
        display_survey_questions()
    elif(option == 2):
        tabulate_survey_response_results()

        average = get_course_average()
        print("Course average: ", average)

        rating = get_faculty_rating(average)
        print("Rating: ", rating)

    elif(option == 3):
        print('Exiting...')
    else:
        print('Invalid option ...')

def display_survey_questions():
    survey_id = 1

    for question_id, question in survey_questions.items():
        print(question_id, question)

        for option, value in survey_question_options.items():
            print(option, value)
        
        response = input("Enter response: ")
        capture_survey_response(survey_id, question_id, int(response))
        survey_id += 1
        print(survey_responses_list)

def capture_survey_response(survey_id, question_id, response):
    survey_responses_list.append([survey_id, question_id, response])

def tabulate_survey_response_results():
    cnt = 0

    for response in survey_responses_list:
        print(response)

        survey_response_results_total[response[1]] += response[2]

        if '2.5' == response[1]:
            cnt += 1

    print(survey_response_results_total)

    for question_id, totals in survey_response_results_total.items():
        survey_response_results[question_id]  = totals / cnt

    print(survey_response_results)

def get_course_average():
    total_average = 0
    total = 0

    for question_id, average in survey_response_results.items():
        total += average

    total_average = total / len(survey_response_results)

    return total_average

def get_faculty_rating(ratio):

    if (ratio <= 6 and ratio >= 5.5) :

        return 'Excellent'
    elif(ratio >= 5):
        return 'Very Good'

    elif (ratio >= 4):
        return 'Good'

    elif (ratio >= 3):
        return 'Needs Improvement'

    elif (ratio <= 3):
        return 'Unacceptable'
    
    else: 
        return 'Invalid value'
    

def add_customers_to_dictionary():
    customer1 = Customer(123456, 'John', 'Doe')
    customer2 = Customer(789123, 'Mary', 'Doe')
    customer3 = Customer(987654, 'Joe', 'Doe')

    customers = {}
    customers[customer1.get_customer_id()] = customer1.get_customer_name()
    customers[customer2.get_customer_id()] = customer2.get_customer_name()
    customers[customer3.get_customer_id()] = customer3.get_customer_name()

    for key, value in customers.items():
        print(key, value)