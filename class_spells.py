

class skill:
    def __init__(self, name, nature, require_lvl, tree, pick=0, synergy_picks=[], description=''):
        self.name = name
        self.nature = nature
        self.require_lvl = require_lvl
        self.pick = pick
        self.tree = tree
        self.description = description
        self.synergy_picks = synergy_picks

    def init_synergy(self, hero):
        if not self.synergy_picks:
            self.attributs = []
        else:
            self.attributs = {}
            for j in self.synergy_picks:
                for act in hero.active_:
                    if j == act.name:
                        self.attributs[j] = act.pick
                for pas in hero.passive_:
                    if j == pas.name:
                        self.attributs[j] = act.pick


class active_skill(skill):
    def effect(self, f=lambda x: x, dmg=0, type_='casting'):
        self.type_ = type_
        self.f = f
        self.dmg = dmg

    def cast(self):
        if not self.synergy_picks:
            dmg = self.f(self.dmg, self.pick)
            return dmg
        else:
            dmg = self.f(self.dmg, self.pick, self.attributs)
            return dmg

    def stat_skill(self):
        print(self.description)
        print('''
        Name: %s    Nature: %s   Skill level: %s
        Damage: %s
        '''
        %
        (
        self.name,
        self.nature,
        self.require_lvl,
        self.dmg
        ))
        raw_input('enter to continue')


class passive_skill(skill):

    def effect(self, HP_max=0, MP_max=0, armour=0, dmg=0, evasion=0, crit=0, fire_resistance=0, frost_resistance=0, bio_resistance=0, miko_resistance=0):
        standard_add = {}
        standard_add['HP_max'] = HP_max
        standard_add['MP_max'] = HP_max
        standard_add['armour'] = armour
        standard_add['dmg'] = dmg
        standard_add['evasion'] = evasion
        standard_add['crit'] = crit
        self.standard_add = standard_add

        resistance_add = {}
        resistance_add['fire'] = fire_resistance
        resistance_add['frost'] = frost_resistance
        resistance_add['bio'] = bio_resistance
        resistance_add['miko'] = miko_resistance
        self.resistance_add = resistance_add

    def mount(self, hero):
        for i in self.standard_add:
            y = eval('hero.%s'%(i))
            y += self.standard_add[i]*self.pick
        for i in self.resistance_add:
            hero.resistance[i] += self.resistance_add[i]*self.pick

    def unmount(self, hero):
        for i in self.standard_add:
            y = eval('hero.%s' % (i))
            y -= self.standard_add[i]*self.pick
        for i in self.resistance_add:
            hero.resistance[i] -= self.resistance_add[i]*self.pick

    def stat_skill(self):
        print(self.description)
        print('''
        Name: %s   Nature: %s    Skill level: %s
        HP: +%s
        MANA: +%s
        Armour: +%s
        Damage: +%s
        Evasion: +%s
        Crit: +%s
        '''
        %
        (
        self.name,
        self.nature,
        self.require_lvl,
        self.HP_max,
        self.MP_max,
        self.armour,
        self.dmg,
        self.evasion,
        self.crit
        ))
        raw_input('enter to continue')
