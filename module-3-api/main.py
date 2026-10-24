import random
import requests

def pokemon_game():
    pokemon_list = ["Terapagos", "Pecharunt", "Hydrapple", "Munkidori", "Pikachu"]
    target = random.choice(pokemon_list)
    
    try:
        url = f"https://pokeapi.co{target.lower()}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        print(f"Failed to load game data: {e}")
        return

    print(f"\nA wild Pokémon appeared!\nHeight: {data['height']} decimeters\nWeight: {data['weight']} hectograms")
    
    for attempts in range(3, 0, -1):
        guess = input(f"\n[{attempts} left] Who's that Pokémon? ").strip().lower()
        if guess == data['name']:
            print(f"Correct! It was {target}!")
            return
        elif attempts > 1:
            print("Wrong! Try again.")
            
    print(f"Game Over. It was {target}.")

if __name__ == "__main__":
    pokemon_game()
