import random
import json
from pokemon import Pokemon
from type import *


class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def is_over(self):
        return self.pokemon1.get_health() <= 0 or self.pokemon2.get_health() <= 0

    def get_winner_name(self):
        if self.pokemon1.get_health() <= 0:
            return self.pokemon2.get_name()
        else:
            return self.pokemon1.get_name()

    def can_attack(self):
        return random.randint(0, 1)

    def get_multiplier(self, attacker, defender):
        multiplier = 1
        for defender_type in defender.get_type():
            multiplier *= attacker.get_type_effectiveness(defender_type)
        return multiplier

    def deal_damage(self, attacker, defender):
        damage = (2 * attacker.get_level() / 5 + 2) * attacker.get_attack() * \
                 self.get_multiplier(attacker, defender) / defender.get_defense() / 50 + 2
        defender.lose_health(damage)

    def get_loser_name(self):
        if self.pokemon1.get_health() <= 0:
            return self.pokemon1.get_name()
        else:
            return self.pokemon2.get_name()

    def register_pokemon(self, pokemon):
        with open('pokedex.json', 'r+') as file:
            data = json.load(file)
            for p in data['pokemons']:
                if p['name'] == pokemon.get_name():
                    return
            data['pokemons'].append({
                'name': pokemon.get_name(),
                'type': pokemon.get_type(),
                'health': pokemon.get_max_health(),
                'attack': pokemon.get_attack(),
                'defense': pokemon.get_defense(),
                'level': pokemon.get_level()
            })
            file.seek(0)
            json.dump(data, file, indent=4)