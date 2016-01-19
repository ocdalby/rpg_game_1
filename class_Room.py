from random import randint
from class_enemyGenerator import EnemyGenerator
from termcolor import colored
from class_happening import happening as hap, quest_


class Room:
    def __init__(self, name, creatures=None, north=None, east=None, south=None, west=None, region='', proba=50, preposition='', item=None, room_lvl=1, counter_max=10000, quest=quest_()):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.proba = proba
        self.creatures = creatures
        self.item = item
        self.room_lvl = room_lvl
        self.counter_max = counter_max
        self.counter = 0
        self.quest = quest
        self.region = region
        self.preposition = preposition

    def set_north(self, room):
        self.north = room
        room.south = self

    def set_south(self, room):
        self.south = room
        room.north = self

    def set_west(self, room):
        self.west = room
        room.east = self

    def set_east(self, room):
        self.east = room
        room.west = self

    def happening(self, hero):
        if self.counter < self.counter_max:
            if randint(1, 100) <= self.proba and self.creatures != None:
                opponent_index = self.creatures[randint(0, len(self.creatures)-1)]
                opponent_ini = EnemyGenerator(opponent_index)
                opponent = opponent_ini.generate(self.room_lvl, time=hero.time)
                fighting = hero._fight(opponent)
                if fighting == 0:
                    return 0
        self.quest.first(hero)

        if self.item != None:
            pick = raw_input('you found an item: %s , do you wish to pick it up? y/n' % (colored(self.item.name, color='cyan')))
            if pick == 'y':
                hero.pickup(self.item)
                print 'You picked up a %s !' % (colored(self.item.name, 'cyan'))
            else:
                print'you left the %s in the %s' % (colored(self.item.name, 'cyan'), colored(self.name, 'blue'))

    def directions(self):
        if self.north != None:
            up = self.north.name
        else:
            up = 'No way'
        if self.south != None:
            down = self.south.name
        else:
            down = 'No way'
        if self.east != None:
            right = self.east.name
        else:
            right = 'No way'
        if self.west != None:
            left = self.west.name
        else:
            left = 'No way'

        print'west -> %s ; north -> %s ; south -> %s,east -> %s' % (colored(left, 'yellow'), colored(up, 'blue'), colored(down, 'red'), colored(right, 'green'))

    def print_place(self):
        if self.region == 'Anaheim':
            print('''
     _                _          _
    / \   _ __   __ _| |__   ___(_)_ __ ___
   / _ \ | '_ \ / _` | '_ \ / _ \ | '_ ` _  |
  / ___ \| | | | (_| | | | |  __/ | | | | | |
 /_/   \_\_| |_|\__,_|_| |_|\___|_|_| |_| |_|



            ''')
        elif self.region == 'Elanor':
            print('''
  _____ _
 | ____| | __ _ _ __   ___  _ __
 |  _| | |/ _` | '_ \ / _ \| '__|
 | |___| | (_| | | | | (_) | |
 |_____|_|\__,_|_| |_|\___/|_|



            ''')
        elif self.region == 'Plains':
            print('''
  ____  _       _
 |  _ \| | __ _(_)_ __  ___
 | |_) | |/ _` | | '_ \/ __|
 |  __/| | (_| | | | | \__ \.
 |_|   |_|\__,_|_|_| |_|___/
            ''')

        elif self.region == 'Woods':
            print('''
 __        __              _
 \ \      / /__   ___   __| |___
  \ \ /\ / / _ \ / _ \ / _` / __|
   \ V  V / (_) | (_) | (_| \__ \.
    \_/\_/ \___/ \___/ \__,_|___/


            ''')
        elif self.region == 'Mountains':
            print('''
  __  __                   _        _
 |  \/  | ___  _   _ _ __ | |_ __ _(_)_ __  ___
 | |\/| |/ _ \| | | | '_ \| __/ _` | | '_ \/ __|
 | |  | | (_) | |_| | | | | || (_| | | | | \__ \.
 |_|  |_|\___/ \__,_|_| |_|\__\__,_|_|_| |_|___/


            ''')
        elif self.region == 'swamps':
            print('''
  ____
 / ___|_      ____ _ _ __ ___  _ __  ___
 \___ \ \ /\ / / _` | '_ ` _ \| '_ \/ __|
  ___) \ V  V / (_| | | | | | | |_) \__ \.
 |____/ \_/\_/ \__,_|_| |_| |_| .__/|___/
                              |_|


            ''')
