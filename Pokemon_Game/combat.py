from typing import List
from pokemon import Pokemon
from pokedex import Pokedex
from enum import Enum
import random

class Combat:
    def __init__(self, pokedex: Pokedex, joueur2: List[Pokemon]):
        self.pokedex = pokedex
        self.joueur1 = pokedex.obtenir_choix_joueur()
        self.joueur2 = joueur2

    def attaque(self, attaquant: Pokemon, defenseur: Pokemon):
        print(f"{attaquant.nom} attaque {defenseur.nom} !")
        degats = attaquant.attack - defenseur.defense
        if degats > 0:
            defenseur.current_hp -= degats
            print(f"{defenseur.nom} perd {degats} points de vie !")
        else:
            print(f"L'attaque n'a aucun effet...")

        if defenseur.current_hp <= 0:
            print(f"{defenseur.nom} est K.O. !")

    def tour(self):
        print("Tour de jeu !")
        self.attaque(self.joueur1.obtenir_pokemon_actif(), self.joueur2.obtenir_pokemon_actif())
        self.attaque(self.joueur2.obtenir_pokemon_actif(), self.joueur1.obtenir_pokemon_actif())

    def debuter_combat(self):
        while self.joueur1.a_des_pokemons() and self.joueur2.a_des_pokemons():
            self.tour()

        if self.joueur1.a_des_pokemons():
            print("Le joueur 1 a gagné le combat !")
        else:
            print("Le joueur 2 a gagné le combat !")
