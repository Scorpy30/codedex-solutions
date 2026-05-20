# Currency Conversion 💸
# Codédex solutions
# In this example, we will convert amounts from three different currencies (Colombian Pesos, Peruvian Soles, and Brazilian Reais) to US Dollars. We will use the following exchange rates:
# 1 Colombian Peso (COP) = 0.00027 USD
# 1 Peruvian Sol (PEN) = 0.29 USD
# 1 Brazilian Real (BRL) = 0.20 USD

co = int(input("How much do you have left in Colombian Pesos? "))
pe = int(input("How much do you have left in Peruvian Soles?"))
br = int(input("How much do you have left in Brazilian Reais? "))

usd = co * 0.00027 + pe * 0.29 + br * 0.20

print()
print(f"Total amount in USD : {usd}")