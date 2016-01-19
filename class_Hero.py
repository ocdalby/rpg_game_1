import os
from random import randint
from math import exp
from class_LivingThing import LivingThing
from termcolor import colored
from class_items import Item


class Hero(LivingThing):
    def __init__(self, name, hero_class, spells_equip=[], HP_max=100, MP_max=100, evasion=1, magic_armor=10, crit=1, dmg=0, armour=0, time=7, gold=0, experience=0):
        self.name = colored(name, 'blue', attrs=['blink'])
        self.HP_max = HP_max
        self.HP = HP_max
        self.MP_max = MP_max
        self.MP = MP_max
        self.hunger = 0
        self.armour = armour
        self.dmg = dmg
        self.evasion = evasion
        self.gold = gold
        self.crit = crit
        self.experience = experience
        self.level = 1
        self.name_save = name
        self.spells_equip = spells_equip
        self.time = time
        self.hour = 7
        self.day = 0
        self.magic_armor = magic_armor
        self.hero_class = hero_class
        self.active_ = hero_class.skill_active
        self.passive_ = hero_class.skill_passive


        #resistance vector
        resistance = {}
        resistance['fire'] = 0
        resistance['frost'] = 0
        resistance['bio'] = 0
        resistance['miko'] = 0
        self.resistance = resistance



        # self assigned variables
        spec = {}
        spec['shield'] = Item(nature='shield')
        spec['sword'] = Item(nature='sword')
        spec['helmet'] = Item(nature='helmet')
        spec['armour'] = Item(nature='armour')
        spec['legs'] = Item(nature='legs')
        spec['boots'] = Item(nature='boots')
        self.spec = spec
        inventory = {}
        inventory['slot1'] = Item()
        inventory['slot2'] = Item()
        inventory['slot3'] = Item()
        inventory['slot4'] = Item()
        inventory['slot5'] = Item()
        inventory['slot6'] = Item()
        self.inventory = inventory
        self.item_types = ['shield', 'sword', 'helmet', 'armour', 'legs', 'boots']
        self.inventory_slots = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6']

    def days(self, word=''):
        days = self.time//24
        hour = self.time % 24
        self.day = days
        self.hour = hour
        if hour >= 23:
            print('You had to find a place to sleep and slept for %s hours' % (7+(24-self.hour)))
            self.time += 7+(24-self.hour)
            days = self.time//24
            hour = self.time % 24
            self.day = days
            self.hour = hour
            raw_input('<enter to continue>')

        if word == 'sleep':
            self.time += 7+(24-self.hour)
            print('You slept for %s hours and have replenished your health' % (7+(24-self.hour)))
            days = self.time//24
            hour = self.time % 24
            self.day = days
            self.hour = hour
            raw_input('<enter to continue>')

    def time_action(self):

        self.time += 1
        self.days()

    def save_hero(self, name):

        script_dir = os.path.dirname(__file__)
        rel_path = 'save_files/%s.txt' % (name)
        abs_file_path = os.path.join(script_dir, rel_path)

        file = open(abs_file_path, 'w')
        file.write('%s %s %s %s %s %s %s %s %s %s %s %s %s\n'
        % (
        self.name_save,
        self.HP_max,
        self.HP,
        self.MP_max,
        self.MP,
        self.hunger,
        self.armour,
        self.dmg,
        self.evasion,
        self.gold,
        self.crit,
        self.experience,
        self.level
        ))
        for i in self.spec:
            file.write(self.spec[i].stats_save())
        for i in self.inventory:
            file.write(self.inventory[i].stats_save())
        file.close

    def load_hero(self, filename):

        script_dir = os.path.dirname(__file__)
        rel_path = 'save_files/%s.txt' % (filename)
        abs_file_path = os.path.join(script_dir, rel_path)

        file = open(abs_file_path, 'r')
        hero_inf = file.readline().split()
        specc = []
        for i in range(6):
            specc.append(file.readline().split())
        inv = []
        for i in range(6):
            inv.append(file.readline().split())
        file.close()
        self.name = hero_inf[0]
        self.HP_max = float(hero_inf[1])
        self.HP = float(hero_inf[2])
        self.MP_max = float(hero_inf[3])
        self.MP = float(hero_inf[4])
        self.hunger = float(hero_inf[5])
        self.armour = float(hero_inf[6])
        self.dmg = float(hero_inf[7])
        self.evasion = float(hero_inf[8])
        self.gold = float(hero_inf[9])
        self.crit = float(hero_inf[10])
        self.experience = float(hero_inf[11])
        self.level = float(hero_inf[12])

        for i in specc:
            a = i[0]
            b = i[1]
            c = float(i[2])
            d = float(i[3])
            e = float(i[4])
            f = float(i[5])
            g = float(i[6])
            h = float(i[7])
            j = float(i[8])
            self.spec[a] = Item(nature=a, name=b, cost=j, add_arm=d, add_HP=e, add_MP=f, add_evasion=g, add_crit=h, add_dmg=c)
        l = 1
        for i in inv:
            a = i[0]
            b = i[1]
            c = float(i[2])
            d = float(i[3])
            e = float(i[4])
            f = float(i[5])
            g = float(i[6])
            h = float(i[7])
            j = float(i[8])
            ind = 'slot%s' % (l)
            print ind
            self.inventory[ind] = Item(nature=a, cost=j, add_arm=d, add_HP=e, add_MP=f, add_evasion=g, add_crit=h, add_dmg=c)
            l += 1

    def skill_tree(self, choice_):
        choice = choice_
        if choice == 'active':
            picks = []
            for i in self.active_:
                if self.level >= i.require_lvl:
                    good = 0
                    for k in i.tree:
                        if k != None:
                            if k.pick > 0:
                                good += 1
                            if good == len(i.tree)-1:
                                picks.append(i)
            print('''
              ____  _    _ _ _                  _        _   _
             / ___|| | _(_) | |___             / \   ___| |_(_)_   _____
             \___ \| |/ / | | / __|  _____    / _ \ / __| __| \ \ / / _ \.
              ___) |   <| | | \__ \ |_____|  / ___ \ (__| |_| |\ V /  __/
             |____/|_|\_\_|_|_|___/         /_/   \_\___|\__|_| \_/ \___|

            ''')
            print('%10s %10s %10s %10s' % ('name', 'nature', 'lvl', '+'))
            for i in picks:
                print('%10s %10s %10s %10s' % (i.name, i.nature, i.require_lvl, i.pick))
            jeb = True
            while jeb:
                y = raw_input('which spell to +1 ? type name:')
                if not y:
                    print'you must enter a name'
                else:

                    for x in self.active_:
                        if x.name == y:
                            x.pick += 1
                            raw_input('''
                            %s +1 !
                            <enter to continue>
                            '''
                            % (x.name))
                            for j in self.active_:
                                j.init_synergy(self)
                            jeb = False
                    if jeb:
                        print'%s is not in the list of skills provided' % (y)

        elif choice == 'passive':
            picks = []

            for i in self.passive_:
                if self.level >= i.require_lvl:
                    good = 0
                    for k in i.tree:
                        if k != None:
                            if k.pick > 0:
                                good += 1
                            if good == len(i.tree)-1:
                                picks.append(i)
            print('''
              ____  _    _ _ _               ____               _
             / ___|| | _(_) | |___          |  _ \ __ _ ___ ___(_)_   _____
             \___ \| |/ / | | / __|  _____  | |_) / _` / __/ __| \ \ / / _ \.
              ___) |   <| | | \__ \ |_____| |  __/ (_| \__ \__ \ |\ V /  __/
             |____/|_|\_\_|_|_|___/         |_|   \__,_|___/___/_| \_/ \___|


            ''')
            print('%10s %10s %10s %10s' % ('name', 'nature', 'lvl', '+'))
            for i in picks:
                print('%10s %10s %10s %10s' % (i.name, i.nature, i.require_lvl, i.pick))

            jeb = True
            while jeb:
                y = raw_input('which spell to +1 ? type name:')
                if not y:
                    print'you must enter a name'
                else:

                    for x in self.passive_:
                        if x.name == y:
                            x.unmount(self)
                            x.pick += 1
                            x.mount(self)
                            raw_input('''
                            %s +1 !
                            <enter to continue>
                            '''
                            %
                            (x.name))
                            for x in self.passive_:
                                x.unmount(self)
                                x.mount(self)
                            jeb = False
                    if jeb:
                        print'%s is not in the list of skills provided' % (y)
        else:
            self.skill_tree()

    def equip_skill_active(self, skill):
        print('''
        what spell to to change? type 'name of spell'
        spell 1: %s
        spell 2: %s
        '''
        %
        (
        self.spells_equip[0].name,
        self.spells_equip[1].name
        ))
        y = raw_input('>')
        if not y:
            print('Type something')
        else:
            if y == self.spells_equip[0].name:
                self.spells_equip[0] = skill
                print('spell 1 is now %s' % (skill.name))
                raw_input('<enter to continue>')

            elif y == self.spells_equip[1].name:
                    self.spells_equip[1] = skill
                    print('spell 2 is now %s' % (skill.name))
                    raw_input('<enter to continue>')

            else:
                print'Ortograph!'

    def skill_inf(self):
        print('''
          _   _                      _    _ _ _
         | | | | ___ _ __ ___    ___| | _(_) | |___
         | |_| |/ _ \ '__/ _ \  / __| |/ / | | / __|
         |  _  |  __/ | | (_) | \__ \   <| | | \__ \.
         |_| |_|\___|_|  \___/  |___/_|\_\_|_|_|___/
        ''')

        skill_bool_0 = True
        while skill_bool_0:
            skill_bool = True
            while skill_bool:
                print('''
                - 'active'
                - 'passive'
                - 'back'
                ''')
                y1 = str(raw_input('>'))
                if not y1:
                    print'must type something'
                elif y1 != 'active' and y1 != 'passive' and y1 != 'back':
                    print'ortograph!'
                else:
                    skill_bool_1 = True
                    if y1 == 'active':
                        while skill_bool_1:
                            print('''
                              ____  _    _ _ _                  _        _   _
                             / ___|| | _(_) | |___             / \   ___| |_(_)_   _____
                             \___ \| |/ / | | / __|  _____    / _ \ / __| __| \ \ / / _ \.
                              ___) |   <| | | \__ \ |_____|  / ___ \ (__| |_| |\ V /  __/
                             |____/|_|\_\_|_|_|___/         /_/   \_\___|\__|_| \_/ \___|

                            ''')
                            print('%10s %10s %10s %10s' % ('name', 'nature', 'lvl', '+'))
                            for i in self.active_:
                                    print('%10s %10s %10s %10s' % (i.name, i.nature, i.require_lvl, i.pick))
                            print('''
                            'equip'+'skill name' to equip,only if picked
                            'stat' + 'skill name' check stats for skill
                            'back'
                            ''')
                            y2 = raw_input('>')
                            if not y2:
                                print'Type something'
                            else:
                                y2 = y2.split()
                                if y2[0] == 'equip':
                                    counter = 0
                                    for i in self.active_:
                                        if i.name == y2[-1] and i.pick >= 1:
                                            self.equip_skill_active(i)
                                            counter = 1
                                    if counter == 0:
                                            print'You have not picked %s, or ortograph!' % (y2[-1])

                                elif y2[0] == 'stat':
                                    counter = 0
                                    for i in self.active_:
                                        if y2[-1] == i.name:
                                            counter = 1
                                            i.stat_skill()
                                        if counter == 0:
                                            print('ortograph!')
                                elif y2[0] == 'back':
                                    skill_bool_1 = False

                    elif y1 == 'passive':
                        while skill_bool_1:
                            print('''
                              ____  _    _ _ _               ____               _
                             / ___|| | _(_) | |___          |  _ \ __ _ ___ ___(_)_   _____
                             \___ \| |/ / | | / __|  _____  | |_) / _` / __/ __| \ \ / / _ \.
                              ___) |   <| | | \__ \ |_____| |  __/ (_| \__ \__ \ |\ V /  __/
                             |____/|_|\_\_|_|_|___/         |_|   \__,_|___/___/_| \_/ \___|


                            ''')
                            print('%10s %10s %10s %10s' % ('name', 'nature', 'lvl', '+'))
                            for i in self.passive_:
                                print('%10s %10s %10s %10s' % (i.name, i.nature, i.require_lvl, i.pick))
                            print('''
                            'stat' + 'skill name' check stats for skill
                            'back'
                            ''')
                            y3 = raw_input('>')
                            if not y3:
                                print'Type something'
                            else:
                                y3 = y3.split()
                                if y3[0] == 'stat':
                                    counter = 0
                                    for i in self.passive_:
                                        if y3[-1] == i.name:
                                            counter = 1
                                            i.stat_skill()
                                        if counter == 0:
                                            print('ortoraph!')
                                elif y3[0] == 'back':
                                    skill_bool_1 = False
                                else:
                                    print'%s no command' % (y3[0])
                    elif y1 == 'back':
                        skill_bool_0 = False
                        skill_bool = False

    def lvl_up(self):
        if self.experience >= 10*(1.5**(self.level)):
            self.level += 1
            self.HP_max += 10*(1.5**self.level)
            self.MP_max += 10*(1.5**self.level)
            self.armour += 1
            print('''
                       _.--.    .--._
                     ."  ."      ".  ".
                    ;  ."    /\    ".  ;
                    ;  '._,-/  \-,_.`  ;
                    \  ,`  / /\ \  `,  /
                     \/    \/  \/    \/
                     ,=_    \/\/    _=,
                     |  "_   \/   _"  |
                     |_   '"-..-"'   _|
                     | "-.        .-" |
                     |    "\    /"    |
                     |      |  |      |
             ___     |      |  |      |     ___
         _,-",  ",   '_     |  |     _'   ,"  ,"-,_
       _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
     ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
    !     \  \  \   \                  /   /  /  /     !
    :      \  \  \   \                /   /  /  /      :
            ''')

            print('''
              _                _
             | | _____   _____| |  _   _ _ __
             | |/ _ \ \ / / _ \ | | | | | '_ \.
             | |  __/\ V /  __/ | | |_| | |_) |
             |_|\___| \_/ \___|_|  \__,_| .__/
                                        |_|

            ''')

            y = raw_input('''
            You just leveled to lvl %s !
            you gain:
            max HP + %s
            max MP + %s
            armour + %s
            >enter to continue>
            '''
            %(
            self.level,
            10*(1.5**self.level),
            10*(1.5**self.level),
            1
            ))
            self.skill_tree('active')
            self.skill_tree('passive')

    def _exp(self, opponent):
        self.experience += opponent.XP
        y = raw_input('''
        You just gained %s XP
        ''' % (opponent.XP))
        self.lvl_up

    def pickup(self, item):
        self.show_inventory()
        dele = raw_input('Which slot would you like to replace? if none type "none":').split()
        if dele[-1] == 'none':
            print 'the %s is left behind' % (item.name)
        else:
            self.inventory[dele[-1]] = item
            print('You just picked up the %s' % (item.name))

    def status(self):
        print '%s has %s/%s HP, %s/%s MP, %s evasion, %s damage, %s armour, %s gold, %s lvl and %s Exp' % (
                                                        self.name,
                                                        colored(self.HP, 'green'),
                                                        colored(self.HP_max, 'green'),
                                                        colored(self.MP, 'blue'),
                                                        colored(self.MP_max, 'blue'),
                                                        colored(self.evasion, 'grey'),
                                                        colored(self.dmg, 'red'),
                                                        colored(self.armour, 'green'),
                                                        colored(self.gold, 'yellow'),
                                                        colored(self.level, 'magenta'),
                                                        colored(self.experience, 'cyan')
                                                        )

    def _addGold(self, amount):
        self.gold += amount
        print 'You obtained %s gold!' % (colored(amount, 'yellow', attrs=['blink']))

    def sleep(self):
        self.HP = self.HP_max
        self.MP = self.MP_max

    def _fight(self, opponent):

        print('''
           ____                _           _
          / ___|___  _ __ ___ | |__   __ _| |_
         | |   / _ \| '_ ` _ \| '_ \ / _` | __|
         | |__| (_) | | | | | | |_) | (_| | |_
          \____\___/|_| |_| |_|_.__/ \__,_|\__|
        ''')

        opponent.statement()

        enemy_name = colored(opponent.name, 'magenta', attrs=['blink', 'bold'])
        print'You are combatting a lvl %s %s' % (opponent.lvl, enemy_name)
        winner = 0
        runde = 1
        while True:
            q1 = raw_input('continue')
            print('%s%s; %s %s HP - %s %s HP' % (colored('Round ', 'grey', 'on_white'), colored(runde, 'grey', 'on_white'), self.name, colored(round(self.HP, 1), 'white', 'on_green'), opponent.name, colored(round(opponent.HP, 1), 'white', 'on_red')))
            print'%s is preaparing to attack the %s' % (self.name,opponent.name)
            state_self = raw_input('defensive or offensive? ')
            if state_self == 'offensive':
                print'%s is taking an %s state of combat' % (self.name, colored('offensive', 'grey', 'on_white'))
            else:
                print '%s is taking a %s state of combat' % (self.name, colored('defensive', 'grey', 'on_white'))
            if randint(1, 10) <= 5:
                state_opponent = 'defensive'
                print 'The %s is taking a %s state of combat' % (opponent.name, colored('defensive', 'grey', 'on_white'))
            else:
                state_opponent = 'offensive'
                print 'The %s is taking an %s state of combat' % (opponent.name, colored('offensive', 'grey', 'on_white'))

            y1 = raw_input("Use spells? 'y' / 'n' : ")
            if y1 == 'y':
                val = self.spell_cast(opponent, state_self, state_opponent)

            else:

                raw_input('''
                You are using your melee attack!
                <enter for continue>
                ''')
                val = opponent._takedmg(state_self, state_opponent, self)
            if val == 0:
                print 'The %s has %s pieces of gold' % (opponent.name, colored(round(opponent.inventory['gold']), 'yellow'))
                if 'item' in opponent.inventory:
                    print('the %s has a %s !' % (opponent.name, opponent.inventory['item'].name))
                    answ = raw_input('Would you like to pick up the %s ? y/n' % (opponent.inventory['item'].name))
                    if answ == 'y':
                        self.pickup(opponent.inventory['item'])

                self._addGold(opponent.inventory['gold'])
                self._exp(opponent)

                return 1

            q1 = raw_input('continue')
            print'The %s is attacking %s !' % (opponent.name, self.name)
            q1 = raw_input('continue')

            val = self._takedmg(state_opponent, state_self, opponent)
            if val == 0:
                print('You died')
                return 0
            print'After round %s %s has %.1f health and %s has %.1f health remaining' % (runde, self.name, self.HP, opponent.name, opponent.HP)
            runde += 1

    def spell_cast(self, opponent, state_self, state_opponent):
        print('''
        1: %s
        2: %s
        '''
        %
        (
        self.spells_equip[0].name,
        self.spells_equip[1].name
        ))
        y1 = raw_input("What spell? '1' or '2': ")
        if y1 == '1' or y1 == '2':
            ind = eval(y1)-1
            spell = self.spells_equip[ind]
        else:
            print('no such spell')
            self.spell_cast(opponent, state_self, state_opponent)
        if spell.type_ == 'casting':
            val = self._takedmg_magic(dmg_magic=spell.cast(), state_opponent=state_opponent, state_self=state_self, opponent=opponent)
            return val
        elif spell.type_ == 'casual':
            print('You did no spell and proceed to attack with your melee weapon')

        raw_input('''
        You are using your melee attack!
        <enter for continue>
        ''')
        val = opponent._takedmg(state_self, state_opponent, self)
        return val

    def _takedmg_magic(self, dmg_magic, state_self, state_opponent, opponent):
        if state_opponent == 'offensive':
            state_dmg_opponent = 1.1
        else:
            state_dmg_opponent = 1.
        if state_self == 'offensive':
            state_dmg_self = 1.
        else:
            state_dmg_self = 0.9
        state_dmg = state_dmg_self*state_dmg_opponent

        damaged = dmg_magic*((100-opponent.magic_armor)/100.)*state_dmg

        opponent.HP = opponent.HP - (damaged)
        if opponent.HP <= 0:
            print '%s inflicted %s dmg and the %s is dead!' % (self.name, colored(round(damaged, 1), 'red', attrs=['blink']), opponent.name)
            return 0
        print('%s inflicted %s dmg onto %s whom now has %.1f HP remaining' % (self.name, colored(round(damaged, 1), 'red', attrs=['blink']), opponent.name, opponent.HP))
        return 1

    def _takedmg(self, state_opponent, state_self, opponent):

        if state_opponent == 'offensive':
            state_dmg_opponent = 1.1
        else:
            state_dmg_opponent = 1.
        if state_self == 'offensive':
            state_dmg_self = 1.
        else:
            state_dmg_self = 0.9
        state_dmg = state_dmg_self*state_dmg_opponent

        evasive = randint(int(self.evasion), 100)
        if evasive >= 90:
            evade = 0
            print('%s %s' % (self.name, colored('dodged', 'green', attrs=['blink'])))
        else:
            evade = 1

        damaged = (opponent.dmg)*exp(-self.armour/100.0)*(evade)
        critical = 0
        if randint(int(self.crit), 100) >= 80 and evade == 1:
            critical = 1 + (self.crit/100.)
            print('%s got a critical stike with %s magnitude' % (opponent.name, colored(round(critical+1, 1), 'red', attrs=['blink'])))

        damaged = damaged*(1+critical)*state_dmg

        self.HP = self.HP - (damaged)
        if self.HP <= 0:
            print '%s inflicted %s dmg and the %s is dead!' % (opponent.name, colored(round(damaged, 1), 'red', attrs=['blink']), self.name)
            return 0
        print('%s inflicted %s dmg onto %s whom now has %.1f HP remaining' % (opponent.name, colored(round(damaged, 1), 'red', attrs=['blink']), self.name, self.HP))
        return 1

    def equip(self, spot):
        item = self.inventory[spot]

        nat = item.nature
        if nat == 'quest':
            print('This item cannot be equipped')
        else:
            replacing = self.spec[nat]
            print('You are equipa a new %s' % (item.name))

            self.HP_max += item.add_HP
            self.MP_max += item.add_MP
            self.armour += item.add_arm
            self.dmg += item.add_dmg
            self.evasion += item.add_evasion
            self.crit += item.add_crit

            self.HP_max -= replacing.add_HP
            self.MP_max -= replacing.add_MP
            self.armour -= replacing.add_arm
            self.dmg -= replacing.add_dmg
            self.evasion -= replacing.add_evasion
            self.crit -= replacing.add_crit

            self.inventory[spot] = replacing
            self.spec[nat] = item

    def show_eqipment(self):
        print('Your equipment is')
        for i in self.item_types:
            print'<%s>' % (i)
            self.spec[i].stats_T()

    def show_inventory(self):
        for i in self.inventory_slots:
            print '--<%s>--' % (i)
            self.inventory[i].stats_T()

    def look_inventory(self):
        commands = ['inventory', 'equipment', 'stats', 'back']
        while True:
            print('''
               __  __ _____ _   _ _   _
             |  \/  | ____| \ | | | | |
             | |\/| |  _| |  \| | | | |
             | |  | | |___| |\  | |_| |
             |_|  |_|_____|_| \_|\___/

            ''')
            print('''
            Type what to be consulted
            Menu:
            -'inventory'
            -'stats'
            -'skills'
            -'back'

            ''')
            move = raw_input('>')
            if not move:
                print''
            else:
                move = move.split()

                if move[-1] == 'stats':
                    self.status()
                    q1 = raw_input('press enter for back')

                if move[-1] == 'inventory':
                    print('''
                      ___                      _
                     |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _
                      | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
                      | || | | \ V /  __/ | | | || (_) | |  | |_| |
                     |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                                             |___/

                    ''')

                    inven_bool = True
                    while inven_bool:
                        self.status()
                        self.show_inventory()
                        self.show_eqipment()
                        print("""
                        'equip'+'slotx' to equip item
                        'stats'+'slotx' to see stats of item
                        'back' to go back
                        """)
                        move_1 = raw_input('>')
                        if not move_1:
                            print''
                        else:
                            move_1 = move_1.split()
                            if move_1[0] == 'equip' and move_1[-1] in self.inventory_slots:
                                self.equip(move_1[-1])
                            if move_1[0] == 'stats' and move_1[-1] in self.inventory_slots:
                                self.inventory[move_1[-1]].stats()
                            if move_1[0] == 'back':
                                inven_bool = False

                    q1 = raw_input('press enter for back')

                if move[-1] == 'back':
                    break
                if move[-1] == 'skills':
                    self.skill_inf()


class hero_maker:
    def __init__(self, classes):
        self.classes = classes

    def maker(self,spell):
        print('''
        Baker Loyman felt terrible, the nuasia hit him like a horse qick in the stomach. The customer in front of him
        frowned at the sight of a man obviously suffering from some sort of illness is handling bread and pastries that
        are to be eaten. Baker Loyman thus swiflty moving away from the counter and bursting into the kitchen, hoping that
        his business is not to loose too much of its renowed reputation. He opened the owen containing the next batch of
        loafs and grabbed two of them with his bare hands, he then put them on the counter and proceeded to grab another
        two loafs, putting them on the counter and so on. After all the loafs were neatly aligned on the counter top did he
        proceed to cut them in half with his large kitchen machete like bread slicer. He had just cut the ninth loaf,
        he looked down and what met him made him freeze in horror. Without feeling it had he cut a deep wound into his left hand,
        but without feeling a thing! Then he thaught about the loafs in the oven, he looked immediatly at his hands and saw
        that they were burnt too. The baker thaught that the wound seems rather serious, but found it sort of amusing that
        he did not feel any pain from aquiring it, this could be helpful is what he thought to himself. He went to get some bandage,
        it was all the way on top of his highest shelf, 'Merinda..' he thought annoyilngy to himself, 'she always places things
        we do not frequently need to places where they are impossible to retreive', he climbed onto his good old wooden kitchen
        chair and reached out for the bandage. He felt a freezing breeze. After climbing down from the chair with the seccessfully
        retreived bandage in his hand did he proceed to clean his wound in some of the clean water he had there in the kitchen.
        He thought 'strange how I could not feel the burning loafs nor me cutting myself, but the cold water felt freezing', that
        reminded him about that breeze that swept by, 'where could that come from? The ovens here are all on fire, it should feel
        like a sauna in here'. Another breeze swept by him, but this time he could feel it run from his neck down his spine.
        He froze, stood still like a statue, by the reflection in one of his pots had he seen a black shadow like being looking at him,
        and then dissapearing. He was not alone. He did not know what to do, he could not move, he was too afraid. That's when
        it happened, the breeze again. The door leading into the asloon burst open and in rolled what could only seem as a small batallion
        of the imperial guards. 'Nobody moves, you remain precisely where you are' shouted the guard with the golden stripe
        on his shoulder, an imperial lieutenant. 'Easier done than said' said the greatly reliefed baker jokingly, but he wondered
        'what on Lapis is the imperial guards doing in the middle of the city where his bakery is located', before he could
        continue that thought shouted the lieutenant to him 'did you see something unusual?' though with a worried tone,
        'yes, there was someone just over there' answered the baker while pointing where he had seen that thing. 'However,
        where he pointed did not lead anywhere, so where could it go?' did he think. He then continued to his reply
        'it was perhaps the most frigtning experience I have had, it was something dark like a shaddow, but I could clearly
        see that it was looking at me, the size being like a large human', the lieutenant turned green, 'so it's finally time'
        did a tall gentleman who just entered the room utter. The man wore a dark blue robe, sitting tight like a suit, but still
        somewhat baggy, his distinct shoulders were decorated with a distinct X, the baker knew where this man belong, to the Miko
        sensitive trained for combat, the Velcros, or better know amongst the people as dark wizards. 'They know we are here,take the baker away,
        they are using him to get additional information about.', then his tone became much more serious and he finally said
        'Now it's only a question about time'.

        Lapis is a strange place.
        Lucky for you that you grew up in Altaheim, located fairly hidden away in
        the colossal chain of fog mountains.

        ''')
        name = raw_input('''
        Your name:
        ''')

        hero_class_ = self.choose_class()
        return Hero(name, hero_class=hero_class_, spells_equip=[spell, spell], armour=5, dmg=30)

    def choose_class(self):
        print('''
        'inf' + 'name of class', for info
        'pick' + 'name of class', to choose class
        ''')
        for i in self.classes:
            print i.name
        y = raw_input('>')
        if not y:
            print('print something')
            raw_input('<enter to continue>')
            return self.choose_class()
        else:
            y = y.split()
            if y[0] == 'pick':
                for k in self.classes:
                    if y[-1] == k.name:
                        k.intro()
                        return k
                return self.choose_class()

            elif y[0] == 'inf':
                for k in self.classes:
                    if y[-1] == k.name:
                        print(k.description)
                        raw_input('<enter continue>')

            else:
                return self.choose_class()
        return self.choose_class()
