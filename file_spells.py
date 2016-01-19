
__all__ = ['flash_f', 'fireball_f']


"""
Mage spells
"""

"""ACTIVE"""
flash_f = lambda dmg, pick, list: dmg*pick*10

fireball_f = lambda dmg, pick, list: dmg*(pick**2)
