
import random
import requests

pokemon_list = [
    "pikachu",
    "charizard",
    "bulbasaur",
    "squirtle",
    "gengar"
]

def get_pokemon_data(pokemon_name):
    """Get Pokemon information from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            return {
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"]
            }

        elif response.status_code == 404:
            print(f"Pokemon '{pokemon_name}' was not found.")
            return None

        else:
            print(f"API request failed. Status: {response.status_code}")
            return None

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")
        return None

    except (ValueError, KeyError):
        print("Could not read the Pokemon data.")
        return None


def play_game():
    print("================================")
    print("       WHO'S THAT POKEMON?")
    print("================================")
    print("Guess the Pokemon using its height and weight!")
    print("You have 3 attempts. Good luck!\n")

    selected_name = random.choice(pokemon_list)
    pokemon = get_pokemon_data(selected_name)

    if pokemon is None:
        print("The game could not start. Please try again later.")
        return

    print(f"Height: {pokemon['height'] / 10:g} meters")
    print(f"Weight: {pokemon['weight'] / 10:g} kilograms\n")

    for attempt in range(1, 4):
        guess = input(
            f"Attempt {attempt}/3 - Who's that Pokemon? "
        ).strip().lower()

        if not guess:
            print("Please enter a Pokemon name.\n")
            continue

        guessed_pokemon = get_pokemon_data(guess)

        if guessed_pokemon is None:
            print("Please enter a valid Pokemon name and try again.\n")
            continue

        if guess == pokemon["name"]:
            print("\nCorrect! You guessed it!")
            print(
                f"Who's that Pokemon? "
                f"It's {pokemon['name'].capitalize()}!"
            )
            return

        remaining = 3 - attempt

        if remaining > 0:
            print(
                f"Wrong guess! You have {remaining} "
                f"attempt(s) left.\n"
            )
        else:
            print("\nGame over! You used all 3 attempts.")

    print(f"The correct Pokemon was {pokemon['name'].capitalize()}.")


if __name__ == "__main__":
    play_game()
