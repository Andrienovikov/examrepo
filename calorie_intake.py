# Calculating my calorie intake
breakfast = input("Breakfast: ")
lunch = input("Lunch: ")
dinner = input("Dinner: ")
norm = 2500
intake = int(breakfast) + int(lunch) + int(dinner)


def instr():
    if intake < norm:
        print("you should eat more")
        left = int(norm) - int(intake)
        print(left)

    else:
        print("you're doing great")


print(instr())
