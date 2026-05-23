# Magic 8 Ball 🎱
# Codédex explorations

import random

question = input("Question: ")

answers = {
    1: "Yes - definitely",
    2: "It is decidedly so",
    3: "Without a doubt",
    4: "Reply hazy, try again",
    5: "Ask again later",
    6: "Better not tell you now",
    7: "My sources say no",
    8: "Outlook not so good",
    9: "Very doubtful"
}

random_number = random.randint(1, 9)

print(f"Magic 8 Ball: {answers[random_number]}")