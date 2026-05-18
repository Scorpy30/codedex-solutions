# Coin Flip 🪙
# Codédex solutions
# In this example, we will simulate a coin flip using the `random` module in Python. 
# The `random` module provides a function called `randint()` which can be used to generate a random integer between a specified range. 
# We will use this function to generate a random number between 0 and 1, where : 
# 1 represents "Heads" and 0 represents "Tails".

import random
num = random.randint(0, 1)

if num > 0.5:
  print('Heads')
else:
  print('Tails')