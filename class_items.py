from random import randint
from math import exp
from termcolor import colored

class Item:
    def __init__(self,nature='none',name='none',cost=100,add_arm=0,add_HP=0,add_MP=0,add_evasion=0,add_crit=0,add_dmg=0):

        self.nature = nature
        self.cost = cost
        self.add_arm = add_arm
        self.add_HP = add_HP
        self.add_MP = add_MP
        self.add_evasion=add_evasion
        self.add_crit=add_crit
        self.add_dmg=add_dmg

        if name=='none':
            self.name_save = nature
            self.name=colored(nature,'magenta',attrs=['blink'])
        else:
            self.name_save = name
            self.name=colored(name,'magenta',attrs=['blink'])


    def stats(self):
        print('''
        name %s
        dmg  %s
        armour %s
        HP %s
        MP %s
        evasion %s
        crit %s
        ''' % (
        self.name,
        self.add_dmg,
        self.add_arm,
        self.add_HP,
        self.add_MP,
        self.add_evasion,
        self.add_crit
        ))
        q1=raw_input('space to continue')

    def stats_T(self):
        print('name: %s dmg:  %s armour: %s HP: %s MP: %s evasion: %s crit: %s' % (
        self.name,
        self.add_dmg,
        self.add_arm,
        self.add_HP,
        self.add_MP,
        self.add_evasion,
        self.add_crit
        ))
    def stats_save(self):
        y=str('%s %s %s %s %s %s %s %s %s\n'
        %
        (
        self.nature,
        self.name_save,
        self.add_dmg,
        self.add_arm,
        self.add_HP,
        self.add_MP,
        self.add_evasion,
        self.add_crit,
        self.cost
        ))
        return y


class Item_Generator:
    def __init__(self,index=0):
        self.index=index
        self.dict=['shield','sword','helmet','armour','legs','boots']

    def Generate(self,lvl_creep=1):
        index = self.index
        if index==0:
            lvl=randint(1,10)*(lvl_creep/5.)
            typ=randint(0,5)
            dim_arm=1
            sup_dmg=0
            if typ==1:
                sup_dmg=1
                dim_arm=0
            item = Item(
            nature=self.dict[typ],
            cost=100*lvl,
            add_arm=2*dim_arm*lvl,
            add_HP=20*lvl*dim_arm,
            add_MP=10*lvl*dim_arm,
            add_evasion=1*sup_dmg*lvl,
            add_crit=1*sup_dmg*lvl/10.,
            add_dmg=10*sup_dmg*lvl
            )
            return item
        elif index ==1:
            item=Item(name='koobaks tooth',nature='quest')
            return item
