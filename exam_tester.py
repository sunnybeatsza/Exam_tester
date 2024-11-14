import random


def read_file(text):
    with open(text) as questions:
        list_of_questions = questions.readlines()

        return list_of_questions

def set_questions(questions):
    return random.sample(questions, k=10)

def check_answers():
    pass

def produce_marks():
    pass


def exam_tester(text):
    questions = read_file(text)
    questions_list = set_questions(questions)
    for question in questions_list:
        print(question)

    
exam_tester("Questions for CompTia Security.txt")