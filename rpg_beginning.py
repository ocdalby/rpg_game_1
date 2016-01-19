from random import randint
from math import exp
from class_Room import Room
from class_Hero import Hero, hero_maker
from termcolor import colored
from class_items import Item,Item_Generator
from class_spells import skill,  active_skill, passive_skill
from class_happening import happening, quest_
from class_info import help_
from class_classes import classes
from file_spells import *

normal = active_skill(name='nothing', nature='casual', require_lvl=0, tree=None)
normal.effect(type_='casual')

flash = active_skill(name='flash', nature='fire', require_lvl=0, tree=[normal])
flash.effect(dmg=10, f=flash_f)
fireball = active_skill(name='fireball', nature='fire', require_lvl=2, tree=[normal, flash])
fireball.effect(dmg=20, f=fireball_f)

tactic = passive_skill(name='tactic', nature='physical', require_lvl=0, tree=[normal])
tactic.effect()
stinging = passive_skill(name='stinging', nature='physical', require_lvl=1, tree=[normal, tactic])
stinging.effect()

pyro_passive = [tactic, stinging]
pyro_active = [flash, fireball]
Pyro = classes(name='Pyro', sup='Velcros', skill_passive=pyro_passive, skill_active=pyro_active, description='deadly')
hero_classes = [Pyro]


hero = hero_maker(hero_classes).maker(normal)
_help = help_(hero)
_help.print_dragon()


enemy = [0]
enemy_1 = [0, 1]
enemy_2 = [i for i in range(3)]
enemy_3 = [i for i in range(4)]


Goblins = [0]
Rootlets = [1]
Lizards = [2]
Peasants = [3]
Rats = [4]
Forsaken_trees = [5]
Frogling = [6]
RefElf = [7]
MountainTroll = [8]
Amphidels = [9]
Centaur = [10]

boss_1 = [100]

directions = ['north', 'west', 'south', 'east']

quest_1_msg1 = ('''
We have seen recently that many of the city's most precious supplies are not
arriving; food, clothes, metal and other important recources do not reach us!
The imperial guards have told us that there is a beast interupting the supply
lines coming from the Elanor. They think it must have a hive somewhere in the
mountains or in the dark forrest. %s, can you interrogate this ? We need help
'''
%
(hero.name))

quest_1_msg2 = ('''
%s.... oh my, I cannot believe that such a hideous beast even existed, thank you
very much, the city owes great thanks to you! May you have fortune on your climb!
'''
%
(hero.name))

quest_1a=quest_(name='the beat and the trail',step_1=quest_1_msg1,step_2=quest_1_msg2,quest_item_name='koobaks tooth',on=1)

quest_1b_msg1= '''
You walk over to the faul creature, the monster, and rip out one of its teeth as
proof of its immense size.
<return to the barracks>
'''
quest_1b_msg2='''Nothing but a terrible smell here'''


quest_1b=quest_(name='koobaks response',step_1=quest_1b_msg1,step_2=quest_1b_msg2,on=1)


"""
From line 93: setting the map
"""

rooms = {}
rooms['home'] = Room(name='home',preposition='at',region='Anaheim',proba=0)
rooms['middle street'] = Room(name='middle street',preposition='in',region='Anaheim',proba=100,creatures=[0])
rooms['town square'] = Room(name='town square',preposition='at the',proba=20,creatures=Peasants)
rooms['rue 5'] = Room(name='rue 5',preposition='in',proba=0)
rooms["felixs cross"] = Room(name="felixs cross",preposition='at',proba=0)
rooms['gate'] = Room(name='gate',preposition='at the',proba=10,creatures=Peasants,room_lvl=2)

rooms['mr Khan'] = Room(name='mr Khan',preposition='at',proba=0)
rooms['rue 2'] = Room(name='rue 2',preposition='in',proba=0)
rooms['boulangerie'] = Room(name='boulangerie',preposition='at the',proba=0)
rooms['cemetery gates'] = Room(name='cemetery gates',preposition='at the',proba=50,creatures=Rats,room_lvl=1)
rooms['cemetery'] = Room(name='cemetery',preposition='at the',proba=30,creatures=Rats,room_lvl=4)
rooms['Bank imperiale'] = Room(name='Bank imperiale',preposition='at the',proba=50,creatures=Peasants,room_lvl=5)
rooms['blacksmith'] = Room(name='blacksmith',preposition='at the',proba=0)
rooms['whitesmith'] = Room(name='whitesmith',preposition='at the',proba=0)

rooms['rue 8'] = Room(name='rue 8',preposition='at',proba=30,creatures=Peasants)
rooms["newtons square"] = Room(name="newtons square",preposition='in',proba=0)
rooms['barracks'] = Room(name='barracks',preposition='at the',proba=0,quest=quest_1a)
rooms['rue 3'] = Room(name='rue 3',preposition='in',proba=0)
rooms['Keyne square'] = Room(name='Keyne square',preposition='at',proba=10,creatures=Peasants,room_lvl=2)
rooms['college of Altaheim'] = Room(name='college of Altaheim',preposition='at the',proba=0,item=Item_Generator().Generate())
rooms['watchmaker'] = Room(name='watchmaker',preposition='at the',proba=0)
rooms["williams square"] = Room(name="williams square",preposition='in',proba=0)
rooms['beast pit'] = Room(name='beast pit',preposition='in the',proba=0)
rooms["stans home"] = Room(name="stans home",preposition='at',proba=0)



rooms['road'] = Room(name='road',preposition='on the', creatures=enemy_2,proba=10,room_lvl=3)
rooms['farmland'] = Room(name='farmland',preposition='in the',proba=60,creatures=enemy_2,room_lvl=2)
rooms['east path'] = Room(name='east path',preposition='on the',proba=10,creatures=enemy_3,room_lvl=2)
rooms['windy forrest'] = Room(name='windy forrest',preposition='in the',proba=20,creatures=[0,1,2,4,5],room_lvl=2)
rooms['lake'] = Room(name='lake',preposition='by the',proba=30,creatures=[9])
rooms['den'] = Room(name='den',preposition='in the',proba=100,creatures=boss_1,counter_max=1,quest=quest_1b)
rooms['deep forrest'] = Room(name='deep forrest',preposition='in the',proba=70,creatures=[1,5],room_lvl=5)
rooms['elanor forrest'] = Room(name='elanor forrest',preposition='in',proba=20,creatures=[7,1,0,2,4])
rooms['elanor pass'] = Room(name='elanor pass',preposition='in',proba=10,creatures=[7])
rooms['elanor highway'] = Room(name='elanor highway',preposition='on',proba=20,creatures=[7,8])
rooms['mountain of elanor'] = Room(name='mountain of elanor',preposition='on',proba=30,creatures=[8])
rooms['east marsh'] = Room(name='east marsh',preposition='on the',proba=30,creatures=[0,1,2],room_lvl=5)
rooms['marsh'] = Room(name='marsh',preposition='on the',proba=10,creatures=[0,1,10],room_lvl=1)
rooms['swamp'] = Room(name='swamp',preposition='in the',proba=40,creatures=[6,0,1,2],room_lvl=4)
rooms['lilly trail'] = Room(name='lilly trail',preposition='on the',proba=10,creatures=[6,2])
rooms['pond'] = Room(name='pond',preposition='by the',proba=90,creatures=[6])
rooms['academy of wizardy'] = Room(name='academy of wizardy',preposition='at the',proba=0)
rooms['goldsmith'] = Room(name='goldsmith',preposition='at the',proba=0)
Goblins = [0]
Rootlets=[1]
Lizards= [2]
Peasants=[3]
Rats=[4]
Forsaken_trees=[5]
Frogling=[6]
RefElf=[7]
MountainTroll=[8]
Amphidels=[9]
Centaur=[10]


"""
rooms[''].set_east(rooms[''])
rooms[''].set_north(rooms[''])
rooms[''].set_west(rooms[''])
rooms[''].set_south(rooms[''])
"""
rooms['home'].set_east(rooms['middle street'])
rooms['middle street'].set_east(rooms['rue 2'])
rooms['rue 2'].set_east(rooms['boulangerie'])
rooms['rue 8'].set_east(rooms['town square'])
rooms['cemetery gates'].set_east(rooms['cemetery'])
rooms['town square'].set_east(rooms['cemetery gates'])
rooms['newtons square'].set_east(rooms['barracks'])
rooms['whitesmith'].set_east(rooms['rue 5'])
rooms['rue 5'].set_east(rooms['blacksmith'])
rooms['williams square'].set_east(rooms['rue 3'])
rooms['rue 3'].set_east(rooms['felixs cross'])
rooms['felixs cross'].set_east(rooms['gate'])
rooms['gate'].set_east(rooms['road'])
rooms['road'].set_east(rooms['east path'])
rooms['east path'].set_east(rooms['elanor forrest'])
rooms['elanor forrest'].set_east(rooms['elanor pass'])
rooms['windy forrest'].set_east(rooms['deep forrest'])
rooms['deep forrest'].set_east(rooms['den'])
rooms['pond'].set_east(rooms['lilly trail'])
rooms['swamp'].set_east(rooms['marsh'])
rooms['marsh'].set_east(rooms['east marsh'])
rooms['east marsh'].set_east(rooms['mountain of elanor'])
rooms['mountain of elanor'].set_east(rooms['elanor highway'])
rooms['Keyne square'].set_east(rooms['college of Altaheim'])

rooms['academy of wizardy'].set_south(rooms['rue 8'])
rooms['rue 8'].set_south(rooms['newtons square'])
rooms['newtons square'].set_south(rooms['rue 3'])
rooms['rue 3'].set_south(rooms['Keyne square'])
rooms['Keyne square'].set_south(rooms['watchmaker'])
rooms['beast pit'].set_south(rooms['williams square'])
rooms['williams square'].set_south(rooms['stans home'])
rooms['mr Khan'].set_south(rooms['middle street'])
rooms['middle street'].set_south(rooms['town square'])
rooms['town square'].set_south(rooms['rue 5'])
rooms['rue 5'].set_south(rooms['felixs cross'])
rooms['felixs cross'].set_south(rooms['goldsmith'])
rooms['rue 2'].set_south(rooms['cemetery gates'])
rooms['cemetery gates'].set_south(rooms['Bank imperiale'])
rooms['farmland'].set_south(rooms['road'])
rooms['road'].set_south(rooms['lilly trail'])
rooms['lilly trail'].set_south(rooms['marsh'])
rooms['lake'].set_south(rooms['windy forrest'])
rooms['windy forrest'].set_south(rooms['east path'])
rooms['deep forrest'].set_south(rooms['elanor forrest'])
rooms['elanor pass'].set_south(rooms['elanor highway'])

currentroom = rooms['home']

autosave_count = 1
while True:
    _help.print_sword()

    hero.lvl_up()
    currentroom.print_place()
    print('''
    Day: %s time: %s o clock
    You are %s %s
    '''
    %
    (
    hero.day,
    hero.hour,
    currentroom.preposition,
    colored(currentroom.name,'blue')
    ))

    currentroom.directions()

    move = raw_input('>')
    if not move:
        print''
    else:
        move = move.split()

        if move[0] == 'go' and move[-1] in directions:
            if eval('currentroom.%s' % (move[1])) != None:
                hero.time_action()
                currentroom = eval('currentroom.%s' % (move[1]))
                print 'you enter the %s' % (colored(currentroom.name, 'blue'))
                if currentroom.happening(hero) == 0:
                    print 'game over'
                    break
            else:
                print"it's not possible to go that way"
        elif move[0] == 'stat':
            hero.status()
        if move[0] == 'menu':
            hero.look_inventory()
        if move[0] == 'save':
            print('Name of save?')
            y = raw_input('>')
            hero.save_hero(y)
        if move[0] == 'load':
            print('Name of game loaded?')
            y = raw_input('>')
            hero.load_hero(y)

        if move[0] == 'home':
            currentroom = rooms['home']

        if autosave_count % 20 == 0:
            hero.save_hero('autosave')
        autosave_count += 1

        if move[0] == 'sleep' and currentroom.name == 'home':
            hero.days('sleep')
            hero.HP = hero.HP_max
            hero.MP = hero.MP_max
        if move[0] == 'help':
            _help.controls()
