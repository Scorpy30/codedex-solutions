# The Cyclone 🎢
# Codédex solutions
# In this example, we will determine if a person can ride the Cyclone Roller Coaster based on their height and the number of credits they have. The requirements for riding the cyclone are:
# - The person must be at least 137 cm tall.
# - The person must have at least 10 credits.

height = int(input("What is your height(in cm): "))
credits = int(input("How many credits do you have: "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("No requirement met")