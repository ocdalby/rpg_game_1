

class LivingThing:
    def __init__(self, name, inventory, HP=100, MP=100, evasion=1, crit=1, dmg=0, armour=0, experience=0):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.inventory = inventory
        self.hunger = 0
        self.armour = armour
        self.dmg = dmg
        self.evasion = evasion
        self.crit = crit
        self.experience = experience
