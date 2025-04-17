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
