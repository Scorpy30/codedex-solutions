# Currency Conversion 💸
# Codédex solutions

co = int(input("How much do you have left in Colombian Pesos? "))
pe = int(input("How much do you have left in Peruvian Soles?"))
br = int(input("How much do you have left in Brazilian Reais? "))

usd = co * 0.00027 + pe * 0.29 + br * 0.20

print()
print(f"Total amount in USD : {usd}")