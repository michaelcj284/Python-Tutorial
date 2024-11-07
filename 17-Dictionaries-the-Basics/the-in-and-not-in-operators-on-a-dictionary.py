pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
}

print("Electron" in pokemon)

if "Zomnie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The category of Zombie does not exsit!")