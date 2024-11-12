#!usr/bin/env python3

'''
    Writing a Script to DO Spooky Stuff|Jonathan Johnny
'''
def main():
    with open('dracula.txt','r') as vamp: #part one
        draccount = 0
        with open('counted.txt','w') as save:
            for i in vamp.readlines(): #part two
                count = 0
                if "vampire" in i.lower():
                    count =1
                    draccount +=1
                    
                if count == 1:
                    print(i, file=save)
                
    print(draccount)

main()
