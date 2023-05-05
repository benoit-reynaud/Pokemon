from combat import Combat
from pokedex import Pokedex
from pokemon import Pokemon
from graphique import Application
from enum import Enum


class Type(Enum):
    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    EARTH = "earth"
    PLANT = "plant"

# Création des objets Pokemon
bulbizarre = Pokemon("Bulbizarre", Type.PLANT, 120, 20)
salameche = Pokemon("Salameche", Type.FIRE, 100, 25)
carapuce = Pokemon("Carapuce", Type.WATER, 150, 18)

# Création de l'objet Pokedex
pokedex = Pokedex()

# Ajout des Pokemons dans le Pokedex
pokedex.ajouter_pokemon(bulbizarre)
pokedex.ajouter_pokemon(salameche)
pokedex.ajouter_pokemon(carapuce)

if __nom__ == '__main__':
    joueur1 = [bulbizarre, salameche]
    joueur2 = [carapuce, Pokemon("Pikachu", Type.NORMAL, 80, 30)]
    
    for pokemon in joueur1:
        pokedex.ajouter_pokemon(pokemon)

    for pokemon in joueur2:
        pokedex.ajouter_pokemon(pokemon)

    combat = Combat(pokedex, joueur2) # initialisation de l'objet Combat avec les joueurs 1 et 2
    
    combat.debuter_combat() # lancement du combat

