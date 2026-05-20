# Formatted Strings
# Codédex explorations

print("             Student Profile Card               ")
print("||============================================||")
print("||                                            ||")

print(f"{'Enter Name':>25}:", end=" ")
name = input()

print(f"{'Enter Age':>25}:", end=" ")
age = int(input())

print(f"{'Enter CGPA':>25}:", end=" ")
cgpa = float(input())

print("||                                            ||")
print("||============================================||")


print("             Student Profile Card               ")
print("||============================================||")
print("||                                            ||")
print(f"{'Name':>20}: {name}")
print(f"{'Age':>20}: {age}")
print(f"{'CGPA':>20}: {cgpa:.2f}") #2 decimal place only
print("||                                            ||")
print("||============================================||")
