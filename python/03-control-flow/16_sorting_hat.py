# Sorting Hat 🎩
# Codédex solutions
# In this example, we will create a simple sorting hat program that assigns a user to one of the four Hogwarts houses (Gryffindor, Hufflepuff, Ravenclaw, or Slytherin) based on their answers to a series of questions. The program will keep track of points for each house and determine the final house assignment based on the highest points.

points_g = 0
points_r = 0
points_h = 0
points_s = 0

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

option = int(input())
if option == 1:
  points_g = points_g + 1
  points_r = points_r + 1
elif option == 2:
  points_h = points_h + 1
  points_s = points_s + 1
else:
  print('Wrong input')

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

option = int(input())
if option == 1:
  points_h = points_h + 2
elif option == 2:
  points_s = points_s + 2
elif option == 3:
  points_r = points_r + 2
elif option == 4:
  points_g = points_g + 2
else:
  print('Wrong input')

print("Q3)  Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

option = int(input())
if option == 1:
  points_s = points_s + 4
elif option == 2:
  points_h = points_h + 4
elif option == 3:
  points_r = points_r + 4
elif option == 4:
  points_g = points_g + 4
else:
  print('Wrong input')

print(f'Gryffindor: {points_g}')
print(f'Hufflepuff: {points_h}')
print(f'Ravenclaw: {points_r}')
print(f'Slytherin: {points_s}')