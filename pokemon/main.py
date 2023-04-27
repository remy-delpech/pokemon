import json
import random
from pokemon import Pokemon
from type import Normal, Feu, Eau, Terre
from combat import Combat

# Chargement des données de pokemon.json
with open('pokemon.json', 'r') as f:
    data = json.load(f)

# Création des objets Pokemon à partir des données du fichier
pokemons = []
for pokemon_data in data:
    name = pokemon_data['name']
    pv = pokemon_data['pv']
    type = pokemon_data['type']
    att = pokemon_data['att']
    df = pokemon_data['df']
    if type == 'normal':
        pokemon = Normal(name, pv, att, df)
    elif type == 'feu':
        pokemon = Feu(name, pv, att, df)
    elif type == 'eau':
        pokemon = Eau(name, pv, att, df)
    elif type == 'terre':
        pokemon = Terre(name, pv, att, df)
    pokemons.append(pokemon)

# Menu principal
while True:
    print("Menu principal :")
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Accéder au Pokédex")
    print("4. Quitter")
    choix = input("Votre choix : ")

    if choix == '1':
        # Sélection du Pokémon du joueur
        print("Liste des Pokémon disponibles :")
        for i, pokemon in enumerate(pokemons):
            print(f"{i+1}. {pokemon.nom}")
        choix_pokemon = int(input("Sélectionnez votre Pokémon : ")) - 1
        joueur = pokemons[choix_pokemon]

        # Sélection aléatoire du Pokémon adversaire
        adversaire = random.choice(pokemons)

        # Lancement du combat
        combat = Combat(joueur, adversaire)
        combat.lancer()

    elif choix == '2':
        # Ajout d'un Pokémon dans le fichier pokemon.json
        nom = input("Nom du Pokémon : ")
        pv = int(input("Points de vie : "))
        print("Type du Pokémon :")
        print("1. Normal")
        print("2. Feu")
        print("3. Eau")
        print("4. Terre")
        choix_type = int(input("Sélectionnez le type : "))
        if choix_type == 1:
            type = 'normal'
        elif choix_type == 2:
            type = 'feu'
        elif choix_type == 3:
            type = 'eau'
        elif choix_type == 4:
            type = 'terre'
        att = int(input("Puissance d'attaque : "))
        df = int(input("Défense : "))
        pokemon_data = {'name': nom, 'pv': pv, 'type': type, 'att': att, 'df': df}
        data.append(pokemon_data)
        with open('pokemon.json', 'w') as f:
            json.dump(data, f)

    elif choix == '3':
    # Affichage du Pokédex
        types = ['normal', 'feu', 'eau', 'terre']
        for type in types:
            nb_pokemon = len([p for p in pokemons if p.type == type])
        print(f"{type.capitalize()} : {nb_pokemon} Pokémon")
        print("Liste des Pokémon :")
        for pokemon in pokemons:
            print(f"- {pokemon.nom} ({pokemon.type}), {pokemon.pv} PV, {pokemon.att} attaque, {pokemon.df} défense")

    elif choix == '4':
    # Quitter le jeu
        print("À bientôt !")
        break

    else:
        print("Choix invalide, veuillez réessayer.")
                  
# Importation des classes
from pokemon import Pokemon
from type import Normal, Feu, Eau, Terre
from combat import Combat

# Fonction pour ajouter un nouveau Pokémon au fichier pokemon.json
def ajouter_pokemon():
    nom = input("Entrez le nom du nouveau Pokémon : ")
    type_pokemon = input("Entrez le type du nouveau Pokémon : ")
    attaque = int(input("Entrez l'attaque du nouveau Pokémon : "))
    defense = int(input("Entrez la défense du nouveau Pokémon : "))
    pv = int(input("Entrez le nombre de points de vie du nouveau Pokémon : "))
    nouveau_pokemon = Pokemon(nom, pv)
    nouveau_pokemon.defense = defense
    nouveau_pokemon.attaque = attaque
    if type_pokemon == "Normal":
        type_pokemon = Normal(nouveau_pokemon)
    elif type_pokemon == "Feu":
        type_pokemon = Feu(nouveau_pokemon)
    elif type_pokemon == "Eau":
        type_pokemon = Eau(nouveau_pokemon)
    elif type_pokemon == "Terre":
        type_pokemon = Terre(nouveau_pokemon)
    else:
        print("Type de Pokémon invalide")
        return
    type_pokemon.save()

# Fonction pour afficher le Pokédex
def afficher_pokedex():
    pokemons = Pokemon.load_all()
    print("Pokédex :")
    for pokemon in pokemons:
        print(f"{pokemon.nom} ({pokemon.type}): {pokemon.vie} PV")

# Fonction pour lancer une partie
def lancer_partie():
    pokemons = Pokemon.load_all()
    print("Liste des Pokémons :")
    for index, pokemon in enumerate(pokemons):
        print(f"{index + 1}. {pokemon.nom} ({pokemon.type}): {pokemon.vie} PV")
    pokemon_joueur_index = int(input("Choisissez votre Pokémon (entrez le numéro) : ")) - 1
    if pokemon_joueur_index < 0 or pokemon_joueur_index >= len(pokemons):
        print("Pokémon invalide")
        return
    pokemon_joueur = pokemons[pokemon_joueur_index]
    pokemon_adversaire = Pokemon.load_random()
    print(f"Vous allez combattre {pokemon_adversaire.nom} ({pokemon_adversaire.type}): {pokemon_adversaire.vie} PV")
    combat = Combat(pokemon_joueur, pokemon_adversaire)
    combat.lancer_combat()
    if combat.pokemon_perdant is None:
        print(f"{combat.pokemon_gagnant.nom} a gagné le combat !")
    else:
        print(f"{combat.pokemon_perdant.nom} a perdu le combat...")

# Menu principal
while True:
    print("Menu principal :")
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Accéder au Pokédex")
    choix = input("Votre choix : ")
    if choix == "1":
        lancer_partie()
    elif choix == "2":
        ajouter_pokemon()
    elif choix == "3":
        afficher_pokedex()
    else:
        break