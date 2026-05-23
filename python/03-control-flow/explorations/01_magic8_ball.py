# Magic 8 Ball 🎱
# Codédex explorations

import random

question = input('Question:      ')

random_number = random.randint(1, 9)

print('Magic 8 Ball: ',end="")

match(random_number):
   case 1: print('Yes - definitely')
   
   case 2:  print('It is decidedly so')
   
   case 3: print('Without a doubt')
   
   case 4: print('Reply hazy, try again')
   
   case 5: print('Ask again later')
   
   case 6: print('Better not tell you now')
   
   case 7: print('My sources say no')
   
   case 8: print('Outlook not so good')
   
   case 9: print('Very doubtful')
