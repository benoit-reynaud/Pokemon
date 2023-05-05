import json
import random
from enum import Enum


class Pokemon:
    def __init__(self, nom, pokemon_type, level=1, max_hp=100, current_hp=100, attack=0, defense=0):
        self.nom = nom
        self.type = pokemon_type
        self.level = level
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack = attack
        self.defense = defense

    def get_damage(self, opponent_type, opponent_attack):
        damage = opponent_attack * self.type.damage_multiplier(opponent_type)
        return int(damage)

    def save_to_pokedex(self):
        with open("pokedex.json", "r") as f:
            pokedex = json.load(f)
        for pokemon in pokedex:
            if pokemon["nom"] == self.nom:
                return
        pokedex.append({"nom": self.nom, "type": self.type.nom, "defense": self.defense, "attack": self.attack, "max_hp": self.max_hp})
        with open("pokedex.json", "w") as f:
            json.dump(pokedex, f, indent=4)



class Type:
    def __init__(self, nom, damage_multipliers):
        self.nom = nom
        self.__multipliers = damage_multipliers

    def damage_multiplier(self, opponent_type):
        return self.__multipliers[opponent_type.nom]


class Normal(Type):
    def __init__(self):
        damage_multipliers = {
            "Normal": 1,
            "Fire": 1,
            "Water": 1,
            "Electric": 1,
            "Grass": 1,
            "Ice": 1,
            "Fighting": 1,
            "Poison": 1,
            "Ground": 1,
            "Flying": 1,
            "Psychic": 1,
            "Bug": 1,
            "Rock": 1,
            "Ghost": 0,
            "Dragon": 1,
            "Dark": 1,
            "Steel": 1,
            "Fairy": 1
        }
        super().__init__("Normal", damage_multipliers)

class Fire(Type):
    def __init__(self):
        damage_multipliers = {
"Normal": 1,
"Fire": 0.5,
"Water": 0.5,
"Electric": 1,
"Grass": 2,
"Ice": 2,
"Fighting": 1,
"Poison": 1,
"Ground": 1,
"Flying": 1,
"Psychic": 1,
"Bug": 2,
"Rock": 0.5,
"Ghost": 1,
"Dragon": 1,
"Dark": 1,
"Steel": 2,
"Fairy": 1
}
        super().__init__("Fire", damage_multipliers)

class Water(Type):
    def __init__(self):
        damage_multipliers = {
"Normal": 1,
"Fire": 2,
"Water": 0.5,
"Electric": 1,
"Grass": 0.5,
"Ice": 1,
"Fighting": 1,
"Poison": 1,
"Ground": 2,
"Flying": 1,
"Psychic": 1,
"Bug": 1,
"Rock": 2,
"Ghost": 1,
"Dragon": 0.5,
"Dark": 1,
"Steel": 1,
"Fairy": 1
}
        super().__init__("Water", damage_multipliers)

class Electric(Type):
    def __init__(self):
        damage_multipliers = {
"Normal": 1,
"Fire": 1,
"Water": 2,
"Electric": 0.5,
"Grass": 0.5,
"Ice": 1,
"Fighting": 1,
"Poison": 1,
"Ground": 0,
"Flying": 2,
"Psychic": 1,
"Bug": 1,
"Rock": 1,
"Ghost": 1,
"Dragon": 0.5,
"Dark": 1,
"Steel": 1,
"Fairy": 1
}
        super().__init__("Electric", damage_multipliers)

class Grass(Type):
    def __init__(self):
        damage_multipliers = {
"Normal": 1,
"Fire": 0.5,
"Water": 2,
"Electric": 1,
"Grass": 0.5,
"Ice": 1,
"Fighting": 1,
"Poison": 0.5,
"Ground": 2,
"Flying": 0.5,
"Psychic": 1,
"Bug": 0.5,
"Rock": 2,
"Ghost": 1,
"Dragon": 0.5,
"Dark": 1,
"Steel": 0.5,
"Fairy": 1
}
        super().__init__("Grass", damage_multipliers)

class Ice(Type):
    def __init__(self):
        damage_multipliers = {
            "Normal": 1,
            "Fire": 0.5,
            "Water": 0.5,
            "Electric": 1,
            "Grass": 2,
            "Ice": 0.5,
            "Fighting": 2,
            "Poison": 1,
            "Ground": 1,
            "Flying": 2,
            "Psychic": 1,
            "Bug": 1,
            "Rock": 2,
            "Ghost": 1,
            "Dragon": 2,
            "Dark": 1,
            "Steel": 0.5,
            "Fairy": 1
        }
        super().__init__("Ice", damage_multipliers)
