import random
from icecream import ic

breakfast = ["eggs", "bacon", "oats"]
lunch = ["burrito", "quesadilla", "burger"]
dinner = ["carnitas", "fish", "meatballs"]

def choose_item (lst):
    choice = random.choice(lst)
    lst.pop(lst.index(choice))
    return choice

for i in range(3):
    print("Day" + str(i + 1))
    print("Breakfast: " + choose_item(breakfast))
    print("Lunch: " + choose_item(lunch))
    print("Dinner: " + choose_item(dinner))
    print()
