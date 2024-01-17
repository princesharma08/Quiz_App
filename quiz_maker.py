import json
import random

def load_questions(file_name):
    with open(file_name, 'r') as file:
        questions = json.load(file)
    return questions

def display_question(question):
    print(f"Question: {question['question']}")
    for i, choice in enumerate(question['choices']):
        print(f"{i+1}. {choice}")

def load_keys(file_name):
    with open(file_name, 'r') as file:
        keys = json.load(file)
    return keys

def main():
    questions = load_questions('questions.json')
    random.shuffle(questions)

    keys = load_keys('keys.json')

    score = 0
    for i, question in enumerate(questions):
        display_question(question)
        user_answer = int(input("Enter your answer (1-{0}): ".format(len(question['choices'])))) - 1
        if user_answer == question['answer']:
            score += 1
            if i < len(keys) and keys[i]['answer'] == question['answer']:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is: {}".format(question['choices'][question['answer']]))
        else:
            print("Incorrect. The correct answer is: {}".format(question['choices'][question['answer']]))
            if i < len(keys) and keys[i]['answer'] == question['answer']:
                print("However, you got the correct answer for this question in the key.")

    print("Your final score is: {}/{}".format(score, len(questions)))

if __name__ == "__main__":
    main()