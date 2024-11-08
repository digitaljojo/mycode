#!/usr/env python3

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input("What is your name?\n>")
        num= (input("Pick a number between 1 and 3: "))
        while (not(num.isdigit()) or int(num) > 3 or int(num) <1): #ensures valid input
            num= (input("Invalid input. Please pick a number between 1 and 3: "))
        num = int(num)
            
        if name and num in words.keys():
            print("Hi " +  name.capitalize() + "! Welcome to Day 2 of Python Training!")
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!
main()
