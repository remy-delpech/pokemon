from pokemon import Pokemon


class Type(Pokemon):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)

class Normal(Type):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.hp *= 1
        self.attack *= 1
        self.defense *= 1

class Feu(Type):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.hp *= 1.2
        self.attack *= 1.1
        self.defense *= 0.9

class Eau(Type):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.hp *= 1.1
        self.attack *= 0.9
        self.defense *= 1.1

class Terre(Type):
    def __init__(self, name, hp=100, level=1, attack=0, defense=0):
        super().__init__(name, hp, level, attack, defense)
        self.hp *= 1.3
        self.attack *= 0.8
        self.defense *= 1.2