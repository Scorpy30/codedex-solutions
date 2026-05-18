# Fizz Buzz 🥤🐝
# Codédex solutions
# This program will print the numbers from 1 to 100. But for multiples of three, it will print "Fizz" instead of the number, and for multiples of five, it will print "Buzz". For numbers which are multiples of both three and five, it will print "FizzBuzz".

for i in range (1, 101, 1):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0 and i % 5 != 0:
    print('Fizz')
  elif i % 5 == 0 and i % 3 != 0:
    print('Buzz')
  else:
    print(i)