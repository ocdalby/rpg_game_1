from random import randint
from math import exp
from class_LivingThing import LivingThing
from termcolor import colored
from class_items import Item, Item_Generator


class monsters(LivingThing):
    def lvl(self, _lvl, talk=0, quote=['']):
        self.lvl = _lvl
        self.HP = self.HP*exp(_lvl/10.)
        self.MP = self.MP*exp(_lvl/20.)
        self.armour = self.armour+_lvl
        self.dmg = self.dmg*exp(_lvl/15.)
        self.evasion = self.evasion + 50*(exp(_lvl)/exp(100))
        self.crit = self.crit + exp(_lvl/10.)/exp(10)
        self.XP = 10*exp(_lvl/5.)
        self.inventory['gold'] = self.inventory['gold'] + 10*_lvl
        self.talk = talk
        self.quote = quote
        self.magic_armor = 5

    def _takedmg(self, state_opponent, state_self, opponent):

        if state_opponent == '_attack':
            state_dmg_opponent = 1.1
        else:
            state_dmg_opponent = 1.
        if state_self == '_attack':
            state_dmg_self = 1.
        else:
            state_dmg_self = 0.9
        state_dmg = state_dmg_self*state_dmg_opponent

        evasive = randint(int(self.evasion), 100)
        if evasive >= 90:
            evade = 0
            print('%s %s' % (self.name,colored('dodged','red',attrs=['blink'])))
        else:
            evade = 1

        damaged = (opponent.dmg)*exp(-self.armour/100.0)*(evade)
        critical  = 0
        if randint(int(self.crit),100) >= 80 and evade ==1:
            critical = 1 + (self.crit/100.)
            print('%s got a critical stike with %s magnitude' % (opponent.name, colored(round(critical+1,1),'green',attrs=['blink'])))

        damaged = damaged*(1+critical)*state_dmg

        self.HP = self.HP - (damaged)
        if self.HP <= 0:
            print '%s inflicted %s dmg and the %s is dead!' % (opponent.name,colored(round(damaged,1),'green',attrs=['blink']),self.name)
            return 0
        print('%s inflicted %s dmg onto %s whom now has %.1f HP remaining' % (opponent.name, colored(round(damaged,1),'green',attrs=['blink']),self.name,self.HP))
        return 1

    def statement(self):
        if self.talk ==0:
            for i in self.quote:
                print i
                q1=raw_input('>')
        self.talk+=1


class EnemyGenerator:
    def __init__(self,index):
        self.index = index

    def generate(self,level=1,time=0):
        item=Item_Generator()
        l = level

        if self.index ==0:
            self.Has_item = 0
            _lvl = randint(1+l,4+l)
            monster = monsters(
                name=colored('goblin','red',attrs=['bold']),
                HP=20+(time/20.),
                MP=0,
                inventory={'gold': 5*_lvl},
                dmg=5,
                armour=1,
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
                self.Has_item = 1
            monster.lvl(_lvl)
            b = ('''
            Goblins are green small greatures that are seen as annoying by most
            travelers in Lapis. They will try to steal your things at any opportunity
            and without doubt challenge to a fight, even if their opponent is just
            that much stronger. Their long green ears characterize them from other
            small creatures like gnomes.
            <enter continue>
            ''')
            c ='"Give me everything you have or I WILL KILL YOU HUMAN!"'
            monster.quote=[b,c]
            return monster

        elif self.index ==1:
            _lvl = randint(1+l,5+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('rootlet','red',attrs=['bold']),
                HP=26+(time/9.),
                MP=0,
                inventory={'gold': 5*_lvl},
                dmg=10,
                armour=1,
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            Rootlets are tree like beings, but they look more like the roots of
            a tree without the rest. Having multiple tenktacle like arms allows
            it to grapple most beings with ease. Be careful, they are tough and
            grumpy!
            <enter continue>
            ''')
            c ='"Did you just step on my root? You will pay for this human!"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster


        elif self.index == 2:
            _lvl = randint(1+l,6+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('lizard','red',attrs=['bold']),
                HP=10+(time/15.),
                MP=0,
                inventory={'gold': 10*_lvl},
                dmg=5,
                armour=2,
                evasion=60
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            Lizards are small and quick dinosaur like beings, measuring about a
            meter in lengt. They are quite quick, and might just slip away from
            almost anything trown at them !
            <enter continue>
            ''')
            c ='''"Someone told me that you had eggs fro breakfast, I will make you
            make you think twice about that!"'''
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster

        elif self.index == 10:
            _lvl = randint(14+l,25+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('centaur','red',attrs=['bold']),
                HP=250+(time/5.),
                MP=30,
                inventory={'gold': 10*_lvl, 'item': item.Generate(lvl_creep=_lvl)},
                evasion=20,
                dmg=25,
                armour=10
                )
            monster.lvl(_lvl)
            b = ('''
            This majestic creature is to be feared, they are organized and have both
            pacts and villages, they might just attack you in numbers too! Their strenght
            is their power, being strong like a horse (obsiously) but tactical like
            men, be careful.
            <enter continue>
            ''')
            c ='"You can run but you cannot, no wait, you cannot outrun me"'
            monster.quote=[b,c]
            return monster

        elif self.index ==3:
            _lvl = randint(1+l,3+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('angry peasant','red',attrs=['bold']),
                HP=10+(time/20.),
                MP=0,
                inventory={'gold': 2*_lvl},
                dmg=3,
                armour=1,
                )
            if randint(1,100)>=90:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            The famine has forced some people to their limits, they will pillage anything
            they can find so that they can buy food and get shelter. These peasant
            can also deliver quite the punch!
            <enter continue>
            ''')
            c ='"Guys! This one looks wealthy!"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster

        elif self.index ==4:
            _lvl = randint(4+l,9+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('rats','red',attrs=['bold']),
                HP=40+(time/10.),
                MP=0,
                inventory={'gold': 8*_lvl},
                dmg=12,
                armour=3,
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            They are small, but many. Their bites can erode about anything. Be
            careful.
            <enter continue>
            ''')
            c ='"schtk schtk stchk!"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster

        elif self.index ==5:
            _lvl = randint(6+l,13+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('forsaken tree','red',attrs=['bold']),
                HP=45+(time/5.),
                MP=0,
                inventory={'gold': 5*_lvl},
                dmg=15,
                armour=10,
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            Forsaken trees are like the big brother to rootlets. Don't mess with
            them. They are traitors of the good and seek to trap innocent beings
            within it. Most individuals kill themselves before it manages to capture
            them. Death is an easy escape.
            <enter continue>
            ''')
            c ='"Dont be shy"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster
        if self.index ==100:
            _lvl = 30
            item_q1 = Item_Generator(index=1)
            monster = monsters(
                name=colored('Koobak','red',attrs=['bold']),
                HP=3000+(time),
                MP=200,
                inventory={'gold': 50*_lvl,'item':item_q1.Generate()},
                dmg=150,
                armour=20,
                )
            b = ('''
            Koobak:"Ahhh, what do we have here? Dessert that is responsible enough to return
            to me on its own! Hah, I am sure you will be teasty, just like all the
            proviants and guards I have devouvered."
            <enter continue>
            ''')
            c ='"nom nom nom nom"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster

        elif self.index ==6:
            _lvl = randint(1+l,13+l)
            self.Has_item = 0
            monster = monsters(
                name=colored('frogling','red',attrs=['bold']),
                HP=20+(time/50.),
                MP=0,
                inventory={'gold': 6*_lvl},
                dmg=30,
                armour=10,
                evasion=40
                )
            if randint(1,100)>=50:
                monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
            b = ('''
            Froglings spawn in the swamps, watch out for their tongue, it is sharp!
            Being natural amphibious makes them hard to hit, be careful!
            <enter continue>
            ''')
            c ='"quak!"'
            monster.quote=[b,c]
            monster.lvl(_lvl)
            return monster

        elif self.index ==7:
                _lvl = randint(10+l,25+l)
                self.Has_item = 0
                monster = monsters(
                    name=colored('refugee elf','red',attrs=['bold']),
                    HP=40+(time/10.),
                    MP=0,
                    inventory={'gold': 6*_lvl},
                    dmg=30,
                    armour=5,
                    evasion=20
                    )
                if randint(1,100)>=50:
                    monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
                b = ('''
                They normaly flee from the iron hand of the had of Elanor. Stay
                away from these at all cost, they are refugees and could have been
                anything from blacksmiths to elite solidiers. They seek to loot
                you, they are often poor and hungry.
                <enter continue>
                ''')
                c ='"Un etranger qui est perdu, quel dommage."'
                monster.quote=[b,c]
                monster.lvl(_lvl)
                return monster


        elif self.index ==8:
                _lvl = randint(10+l,25+l)
                self.Has_item = 0
                monster = monsters(
                    name=colored('mountain troll','red',attrs=['bold']),
                    HP=900+(time/5.),
                    MP=0,
                    inventory={'gold': 6*_lvl},
                    dmg=10,
                    armour=25,
                    evasion=0
                    )
                if randint(1,100)>=50:
                    monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
                b = ('''
                Hah, good luck! These guys have merged with the mountain after turning
                to stone every night! Run.
                <enter continue>
                ''')
                c ='"Two birds with one stone. Dinner and gold!"'
                monster.quote=[b,c]
                monster.lvl(_lvl)
                return monster

        elif self.index ==9:
                _lvl = randint(6+l,15+l)
                self.Has_item = 0
                monster = monsters(
                    name=colored('Amphidel','red',attrs=['bold']),
                    HP=100+(time/10.),
                    MP=0,
                    inventory={'gold': 6*_lvl},
                    dmg=40,
                    armour=5,
                    evasion=10
                    )
                if randint(1,100)>=50:
                    monster.inventory['item'] = item.Generate(lvl_creep=_lvl)
                b = ('''
                Evolved from dolphis, but these can stay out of the water for a
                temporary time, they are quite dangerous! And they can walk!
                <enter continue>
                ''')
                c ='"Hmmm, you are dead."'
                monster.quote=[b,c]
                monster.lvl(_lvl)
                return monster
