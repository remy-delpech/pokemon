class Pokemon:
    def __init__(self, name, level=1, attack=0, defense=0):
        self.__name = name
        self.__level = level
        self.__attack = attack
        self.__defense = defense
        self.__max_hp = 100
        self.__current_hp = self.__max_hp

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_current_hp(self):
        return self.__current_hp

    def set_attack(self, attack):
        self.__attack = attack

    def set_defense(self, defense):
        self.__defense = defense

    def set_current_hp(self, current_hp):
        self.__current_hp = current_hp

    def take_damage(self, damage):
        damage -= self.__defense
        damage = max(damage, 1)
        self.__current_hp -= damage

    def is_fainted(self):
        return self.__current_hp <= 0

    def display_info(self):
        print(f"{self.__name} (Level {self.__level})")
        print(f"HP: {self.__current_hp}/{self.__max_hp}")
        print(f"Attack: {self.__attack}")
        print(f"Defense: {self.__defense}")