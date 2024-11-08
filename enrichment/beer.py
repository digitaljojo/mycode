def main():
    beers = input("How many beers ya drinking?!")
    while not(beers.isdigit()) or int(beers) >100 or int(beers) <1:
        print("Let's try that again, bub...")
        beers = input("How many beers ya drinking?\n")
    beers = int(beers)

    for i in range(beers,1,-1):
        beer = i
        print(f"{beer} bottles of beer on the wall, {beer} bottles of beer!\nTake one down, pass it around~")
        beer -=1
        print(f"{beer} bottles of beer on the wall!")
    print("One last bottle of beer on the wall, one last bottle of beer!\nDrink it fast don't fall on your arse!")
    print("And now there's no more beers on the wall~!")
main()
