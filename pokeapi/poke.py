#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print('Here is your pokemon!')
    print(pokeapi['sprites']['front_default'])
    print('\nAnd now for their move list!\n')

    for poke in pokeapi['moves']:
        print(poke['move']['name'], end=', ')
    print('\n\n')

    print('This pokemon has been featured in the following amount of games:')
    print(len(pokeapi['game_indices']))
main()

