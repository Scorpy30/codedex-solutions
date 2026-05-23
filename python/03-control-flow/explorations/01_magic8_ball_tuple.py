# Magic 8 Ball 🎱
# Codédex explorations

import random

question = input("Question: ")

answers = (
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
)

print(f"Magic 8 Ball: {random.choice(answers)}")