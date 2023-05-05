class Pokedex:
    def __init__(self):
        self.pokemons = {}

    def ajouter_pokemon(self, pokemon):
        self.pokemons[pokemon.get_nom()] = pokemon

    def get_pokemon(self, nom):
        return self.pokemons.get(nom)

    def lister_pokemons(self):
        for pokemon in self.pokemons.values():
            print(pokemon.nom)

    def obtenir_choix_joueur(self):
        print("Voici la liste des pokémons disponibles :")
        self.lister_pokemons()

        while True:
            choix = input("Choisissez un pokémon parmi la liste ci-dessus : ")
            pokemon = self.get_pokemon(choix)
            if pokemon is not None:
                return pokemon
            else:
                print("Pokémon invalide. Veuillez choisir un autre pokémon.")