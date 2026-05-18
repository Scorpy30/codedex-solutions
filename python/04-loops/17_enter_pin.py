# Enter Pin 🔑
# Codédex solutions
# This program will ask the user to enter their PIN. If the PIN is incorrect, it will keep asking until the correct PIN is entered.

print('=== BANK OF CODÉDEX ===')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
