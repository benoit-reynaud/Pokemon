from tkinter import *
from pokedex import Pokedex
from pokemon import Pokemon
from combat import Combat

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pokémon Combat")
        self.create_widgets()

    def create_widgets(self):
        self.joueur1_label = Label(self.master, text="Joueur 1")
        self.joueur1_label.grid(row=0, column=0)
        self.joueur2_label = Label(self.master, text="Joueur 2")
        self.joueur2_label.grid(row=0, column=2)

        self.joueur1_pokemon_listbox = Listbox(self.master)
        self.joueur1_pokemon_listbox.grid(row=1, column=0)
        self.joueur2_pokemon_listbox = Listbox(self.master)
        self.joueur2_pokemon_listbox.grid(row=1, column=2)

        self.joueur1_pokemon_listbox.bind('<<ListboxSelect>>', self.on_select_joueur1_pokemon)
        self.joueur2_pokemon_listbox.bind('<<ListboxSelect>>', self.on_select_joueur2_pokemon)

        self.joueur1_pokemon_label = Label(self.master, text="Choisissez un Pokémon")
        self.joueur1_pokemon_label.grid(row=2, column=0)
        self.joueur2_pokemon_label = Label(self.master, text="Choisissez un Pokémon")
        self.joueur2_pokemon_label.grid(row=2, column=2)

        self.joueur1_pokemon_stats_label = Label(self.master, text="")
        self.joueur1_pokemon_stats_label.grid(row=3, column=0)
        self.joueur2_pokemon_stats_label = Label(self.master, text="")
        self.joueur2_pokemon_stats_label.grid(row=3, column=2)

        self.commencer_bouton = Button(self.master, text="Commencer", command=self.commencer_combat)
        self.commencer_bouton.grid(row=4, column=1)

    def on_select_joueur1_pokemon(self, event):
        index = self.joueur1_pokemon_listbox.curselection()[0]
        pokemon = self.joueur1_pokemon_list[index]
        self.joueur1_pokemon_label.config(text=pokemon.nom)
        self.joueur1_pokemon_stats_label.config(text=str(pokemon))

    def on_select_joueur2_pokemon(self, event):
        index = self.joueur2_pokemon_listbox.curselection()[0]
        pokemon = self.joueur2_pokemon_list[index]
        self.joueur2_pokemon_label.config(text=pokemon.nom)
        self.joueur2_pokemon_stats_label.config(text=str(pokemon))

    def commencer_combat(self):
        joueur1_pokemon = self.joueur1_pokemon_list[self.joueur1_pokemon_listbox.curselection()[0]]
        joueur2_pokemon = self.joueur2_pokemon_list[self.joueur2_pokemon_listbox.curselection()[0]]
        combat = Combat(Pokedex(), [joueur1_pokemon, joueur2_pokemon])
        combat.debuter_combat()

        self.master.quit()

    def run(self):
        self.master.mainloop()
