# Sorting Hat 🎩
# Codédex explorations

# points dictionary
points = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}


# questions list
# each question in itself is a dictionary with an option dictionary
questions = [

    {
        "question": "Q1) Do you like Dawn or Dusk?",

        "options": {
            1: ("Dawn", {"Gryffindor": 1, "Ravenclaw": 1}),
            2: ("Dusk", {"Hufflepuff": 1, "Slytherin": 1})
        }
    },

    {
        "question": "Q2) When I\'m dead, I want people to remember me as:",

        "options": {
            1: ("The Good", {"Hufflepuff": 2}),
            2: ("The Great", {"Slytherin": 2}),
            3: ("The Wise", {"Ravenclaw": 2}),
            4: ("The Bold", {"Gryffindor": 2})
        }
    },

    {
        "question": "Q3) Which kind of instrument most pleases your ear?",

        "options": {
            1: ("The violin", {"Slytherin": 4}),
            2: ("The trumpet", {"Hufflepuff": 4}),
            3: ("The piano", {"Ravenclaw": 4}),
            4: ("The drum", {"Gryffindor": 4})
        }
    }

]


for q in questions:

    print()
    print(q["question"])

    for number, option_data in q["options"].items():
        print(f"{number}) {option_data[0]}")

    try:
        choice = int(input("Enter your choice: "))

        if choice not in q["options"]:
            print("Invalid choice")
            continue

        selected_option = q["options"][choice][1]

        for house, score in selected_option.items():
            points[house] += score

    except ValueError:
        print("Enter only integers")


print("\n===== Final Scores =====")

for house, score in points.items():
    print(f"{house}: {score}")