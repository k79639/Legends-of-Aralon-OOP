'''This module handels the logic of all the challenges in the game'''

class Challenge:
    def __init__(self, gameInstance):
        self._game = gameInstance
        self._damageToMonster = None
        self._damageToHero = None
        self._monster = None
        self._hero = None
        self._ai = None

    def battlefield(self):
        self._hero = self._game.getHero()
        self._ai = self._game.getAi()

        if self._game.getChallengeNum() == 1:
            #get monster for the round
            self._monster = self._game.getChallenge1Monster()
            #set strength used for this round
            heroAttribute = self._hero.getStrength()
            aiAttribute = self._ai.getStrength()
            heroAttributeName = "Strength"
            aiAttributeName = "Strength"
            #Introduce challenge and Oriana
            self._game.getScript().orianaAndChallenge1Intro()
            #Dialogues for the first challenge
            self._game.getScript().challenge1Dialogues()

        #Loop round until either one of the character or Monster wins the game
        while self._monster.getHealth() > 0 and (self._hero.getHealth() > 0 or self._ai.getHealth() > 0):

            #Check if both hero can roll for the round
            if self._hero.characterIsAlive() == True and self._ai.characterIsAlive() == True:

                #Ask user to roll for the hero
                input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")
                self._hero.rollDice()
                #Calculate the total roll of the hero 
                totalHeroRoll = self._hero.getRoll() + heroAttribute
                #Ensure total roll does not goes into negative
                totalHeroRoll = max(0, totalHeroRoll)

                #AI rolls on its turn.
                self._ai.rollDice()
                #Calculate the total roll of the Ai 
                totalAiRoll = self._ai.getRoll() + aiAttribute
                #Ensure total roll does not goes into negative
                totalAiRoll = max(0, totalAiRoll)

                #Display user what each character rolled and how outcome is affected by their attribute
                print(f"\n{self._hero.getColorName()} \033[0mrolled {self._hero.getRoll()} modified by {self._hero.getName()} {heroAttributeName} ({heroAttribute}) is {totalHeroRoll}")
                print(f"\n{self._ai.getColorName()} \033[0mrolled {self._ai.getRoll()} modified by {self._ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")

                #Calclate the total damage from both heroes
                self._damageToMonster = totalHeroRoll + totalAiRoll

            elif self._ai.characterIsAlive():
                #AI rolls on its turn.
                self._ai.rollDice()
                #Calculate the total roll of the Ai 
                totalAiRoll = self._ai.getRoll() + aiAttribute
                #Ensure total roll does not goes into negative
                totalAiRoll = max(0, totalAiRoll)

                #Display user what Ai rolled and how outcome is affected by it's attribute
                print(f"\n{self._ai.getColorName()} \033[0mrolled {self._ai.getRoll()} modified by {self._ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")
                
                #Damage given by hero
                self._damageToMonster = totalAiRoll

            elif self._hero.characterIsAlive():
                #Ask user to roll for the hero
                input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")
                self._hero.rollDice()
                #Calculate the total roll of the hero 
                totalHeroRoll = self._hero.getRoll() + heroAttribute
                #Ensure total roll does not goes into negative
                totalHeroRoll = max(0, totalHeroRoll)

                #Display user what Ai rolled and how outcome is affected by it's attribute
                print(f"\n{self._ai.getColorName()} \033[0mrolled {self._ai.getRoll()} modified by {self._ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")
                
                #Damage given by Ai
                self._damageToMonster = totalHeroRoll

            #Call appropriate method according to the damage to the monster
            if self._damageToMonster <= 16:
                self.normalAttack()
            elif self._damageToMonster > 17:
                self.criticalAttack()

            #Now it's monster's turn to attack
            # self.monsterAttack()

    def normalAttack(self):
        
        #Update monster health after damage
        self._monster.updateHealth(self._damageToMonster)
        self._game.getScript().typingEffect(f"\nTogether, {self._hero.getColorName()}\033[0m and {self._ai.getColorName()}\033[0m strike, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")
        self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}'s\033[0m remaining health: {self._monster.getHealth()}.")


    def criticalAttack(self):
        #TODO: give monster ability to deal with critical attack
        pass

    def monsterAttack(self):
        #Get monster's Roll
            self._monster.rollDice()
            monsterRoll = self._monster.getRoll()
