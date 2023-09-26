import random
class Pykemon:
    def __init__(self, name, dexNum, currentHP, baseHP, baseAtk, baseDef, baseSpd):
        self.dexNum = dexNum
        self.name = name
        self.currentHP = currentHP
        self.baseHP = baseHP
        self.baseAtk = baseAtk
        self.baseDef = baseDef
        self.baseSpd = baseSpd

    def attack(self):
        # damage = random.uniform(0.8, 1) * (4 * (self.power * (self.baseAtk / self.baseDef)) / 50) # TORNA MOLT PETIT
        damage = self.baseAtk
        return damage

    def harm(self, damage):
        self.currentHP -= damage

    def heal(self, healing):
        if self.currentHP + healing <= self.maxHP:
            self.currentHP += healing
        else:
            self.currentHP = self.maxHP

    def move(move):
        # TO DO: CREAR Y PROBAR CLASE MOVE 
        pass
