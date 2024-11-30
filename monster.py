'''This module handels the hero's of the game and their logic and inherits from character base class'''
from character import Character

class Monster(Character):
    def __init__(self, name, health, title, coloredName, shields):
        Character.__init__(self, name, health, title, coloredName)
        # self._monsterHaveShield = False
        self._monsterTotalShields = shields

    def getTotalShieldsLeft(self):
        return self._monsterTotalShields
    
    '''This method give monster ability to deal with critical damage'''
    def criticalAtkDefence(self):
        if self._monsterTotalShields > 0:
            monsterName = self.getColorName()
            print(f"\n{monsterName}\033[0m summons a shield to protect himself!\n")
            self._monsterTotalShields -= 1
            return True