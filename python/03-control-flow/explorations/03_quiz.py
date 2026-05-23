# Quiz System 📋
# Codédex explorations


# score dictionary
score = {
    "Shamrock" : 0,
    "Sunflower" : 0,
    "Rose" : 0,
    "Violet" : 0
}

questions = [
    {
        "question" : "1. Which is the capital of India?",

        "options" : {
            1 : "New Delhi",
            2 : "Mumbai"
        },

        "answer" : 1
    },
    
    {
        "question" : "2. Which is the smallest state of India?",

        "options" : {
            1 : "Uttar Pradesh",
            2 : "Goa"
        },

        "answer" : 2
    },

    {
        "question" : "3. What is the Biggest land animal?",

        "options" : {
            1 : "Giraffe",
            2 : "Elephant"
        },

        "answer" : 2
    },
    
    {
        "question" : "4. What is the highest mountain peak in the world?",

        "options" : {
            1 : "Mt. Everest",
            2 : "Mt. K2"
        },

        "answer" : 1
    },

    {

        "question" : "5. What is the tallest statue in the world?",

        "options" : {
            1 : "Statue of Unity",
            2 : "Statue of Liberty"
        },

        "answer" : 1
    }
]
        
# print(questions[0])                    ->  {'Q1': '1. Which is the capital of India?', 'options': {1: 'New Delhi', 2: 'Mumbai'}}
# print(questions[0]["question"])        ->  1. Which is the capital of India?
# print(questions[0]["options"])         ->  {1: 'New Delhi', 2: 'Mumbai'}
# print(questions[0]["options"][1])      ->  New Delhi

# print(type(questions))                 ->  <class 'list'>
# print(type(questions[0]))              ->  <class 'dict'>
# print(type(questions[0]["question"]))  ->  <class 'str'>
# print(type(questions[0]["options"]))   ->  <class 'dict'>

for house in score:
    print(f"\n\nQuiz for house: {house}")
    for q in questions:

        print()
        print(q["question"])

        for number, option_data in q["options"].items():
            print(f"{number}){option_data}")
            
        answer = int(input("Enter the number associated with your answer: "))
        if answer == q["answer"]:
            score[house] += 1
            print("Correct answer!")
        else :
            print("Wrong answer")
    print(score)