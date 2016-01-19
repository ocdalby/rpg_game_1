
class classes:
    def __init__(self, name, sup, skill_passive=[], skill_active=[], description='', introduction=''):
        self.name = name
        self.sup = sup
        self.skill_passive = skill_passive
        self.skill_active = skill_active
        self.description = description
        self.introduction = introduction

    def intro(self):
        print(self.introduction)
        raw_input('<enter to continue>')
