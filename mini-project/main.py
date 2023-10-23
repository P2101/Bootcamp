from abc import ABC, abstractmethod
import random
import time
import logs 

class Pykemon(ABC):
    def __init__(self, name, dexNum, baseHP, baseAtk, baseDef, baseSpd):
        self.dexNum = dexNum
        self.name = name
        self._baseHP = baseHP
        self.currentHP = baseHP
        self.baseAtk = baseAtk
        self.baseDef = baseDef
        self.baseSpd = baseSpd

    @abstractmethod
    def descripcion_juego(self, name):
        pass

    def harm(self, defender):
        damage = self.attack()
        defender.currentHP -= damage
        if defender.currentHP < 0:
            defender.currentHP = 0
        return round(damage)

class Electric(Pykemon):
    def __init__(self, name, dexNum, baseHP, baseAtk, baseDef, baseSpd):
        super().__init__(name, dexNum, baseHP, baseAtk, baseDef, baseSpd)

    def descripcion_juego(self, name):
        return f'Soy {name}, un Pykemon eléctrico!'
    
    def attack(self):
        return round(random.uniform(0.6, 1) * (4 * (self.baseAtk * (self.baseAtk / self.baseDef)) / 50))


class Fire(Pykemon):
    def __init__(self, name, dexNum, baseHP, baseAtk, baseDef, baseSpd):
        super().__init__(name, dexNum, baseHP, baseAtk, baseDef, baseSpd)

    def descripcion_juego(self, name):
        return f'Soy {name}, un Pykemon de fuego!'
    
    def attack(self):
        return round(random.uniform(0.6, 1) * (4 * (self.baseAtk * (self.baseAtk / self.baseDef)) / 50))

class Battle:
    def __init__(self, pykemons):
        self.pykemons = pykemons

    def descripcion_juego(self):
        return 'Bienvenido a Pykemon\n'

    def battle(self):
        while all(pykemon.currentHP > 0 for pykemon in self.pykemons):
            for i in range(len(self.pykemons)):
                attacker = self.pykemons[i]
                defender = self.pykemons[(i + 1) % len(self.pykemons)]

                damage = attacker.harm(defender)
                print(f'{attacker.name} hace un ataque de {damage} a {defender.name}')

                if defender.currentHP <= 0:
                    print(f'{defender.name} ha sido derrotado. {attacker.name} ha ganado!')
                    return logs.get_name([attacker.name, defender.name])

                print(f'La vida de {attacker.name} es {attacker.currentHP} y del {defender.name} es {defender.currentHP}')
                time.sleep(2)

pykemons = [Electric('Pikachu', 1, 18, 18, 5, 4), Fire('Charmander', 4, 18, 18, 5, 4)]
battle = Battle(pykemons)
print(battle.descripcion_juego())
for pykemon in pykemons:
    print(pykemon.descripcion_juego(pykemon.name))
battle.battle()
