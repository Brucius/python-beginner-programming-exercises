import random

bullet_position = 3


def spin_chamber():
    chamber_position = random.randint(1, 6)
    return chamber_position

#  DON'T CHANGE THE CODE ABOVE


def fire_gun():
    chamberPos = spin_chamber()
    if bullet_position == chamberPos:
        print("You are dead!")
    else:
        print("Keep playing")


print(fire_gun())
