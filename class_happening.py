from class_Hero import Hero
from class_items import Item


class happening:
    def __init__(self,name='sunny',step_1='',step_2='',quest_item_name=Item(),c=0,on=0):
        self.name=name
        self.c=0
        self.quest_item_name=quest_item_name
        self.on=on
        self.once=0

class quest_(happening):
    def first(self,hero):
        if self.on != 0:


            print 'Hello %s, I hope that you are doing just fine' % (hero.name)
            print step_1

            if self.once ==1:

                if self.quest_item_name in hero.inventory:
                    hero.inventory[hero.inventory.index(quest_item_name)] = Item()
                    print step_2


            self.once=1
