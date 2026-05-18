# Guess Number 🤷🔢
# Codédex solutions
# This program will ask the user to guess a number between 1 and 10. The user has 5 tries to guess the correct number. If the user guesses the correct number, they win. If they run out of tries, they lose.

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries += 1
  
if guess != 6:
    print('You ran out of tries.')
else:
    print('You got it!')