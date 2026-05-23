# pH Levels 🧪
# Codédex solutions
# In this example, we will determine if a given pH value is acidic, basic, or neutral. The pH scale ranges from 0 to 14, where:
# - A pH value less than 7 indicates an acidic solution.
# - A pH value greater than 7 indicates a basic (alkaline) solution.
# - A pH value of exactly 7 indicates a neutral solution.

ph = (int(input("Enter a ph value between 0 and 14: ")))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')