#!usr/bin/env python3
import random

#see how quickly you can kill a random monster. It will have vunerabilty, resistance, and immunity.
#Give the monster 10 HP.
monster = 10
hero = 10

#Decide on the vunerabilty at random.
weak = random.randint(0,3)

#define the weakness multiplier P/S/B
vun_list = [[1,1,1], [2,1,0.5], [1,0.5,2], [0.5,2,1]]
multiplier = vun_list[weak]

#give them a weapon
def blade():
    #define the weapon
    weapon = int(input("Choose your weapon!\n1-Rapier\n2-Longsword\n3-Hammer\n--->"))
    while (weapon > 3 or weapon <1):
        print("Invalid choice. Please try again.")
        weapon = int(input("Choose your weapon!\n1-Rapier\n2-Longsword\n3-Hammer\n--->"))
    return weapon

weapon = blade()

print("Move to combat!")

turn =1
while (monster > 0):
    print("\n\n TURN",turn,"\n\n")
    dmg = random.randint(0,5) * multiplier[weapon-1] #calcs damage to the monster
    monster = monster - dmg #reduces hitpoints
    if (dmg == (5*multiplier[weapon-1])):
        print("Max damage! The monster has ", monster, " HP remaining!")
        print("Monster HP: ",monster,"/10HP")
    elif (dmg > 2):
        print("You've dealt ", dmg, " damage this turn. The monster has ", monster, " HP remaining!")
        print("Monster HP: ",monster,"/10HP")
    else:
        strike = random.randint(0,10) * 0.5
        hero = hero - strike
        print("You've been hit! You lost ", strike, "HP!")
        print("Monster HP: ", monster,"/10HP")
    if(hero <= 0 or monster <= 0):
        break
    turn = turn +1
    print("Your health: ",hero,"/10HP")
    answer = input("Would you like to switch weapons? \n y/n \n =====>")
    if (answer == 'y'):
        blade()    


if (hero < monster):
    print("You DIED...")
else:
    print("Congratulations brave hunter, it took you ", turn, " turns to win this fight. You have ", hero," remaining.")



