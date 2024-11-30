'''This module handels the logic of all the challenges in the game'''

class Challenge:
    def __init__(self, gameInstance):
        self._game = gameInstance
        self._damageToMonster = None
        self._damageToHero = None
        self._damageToAi = None
        self._monster = None
        self._hero = None
        self._ai = None

    def getMonster(self):
        return self._monster

    '''This is the main method which handels the flow of each challenge'''   
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

        elif self._game.getChallengeNum() == 2:
            #get monster for the round
            self._monster = self._game.getChallenge2Monster()
            #set strength used for this round
            heroAttribute = self._hero.getIntelligence()
            aiAttribute = self._ai.getIntelligence()
            heroAttributeName = "Intelligence"
            aiAttributeName = "Intelligence"
            #Introduce challenge
            self._game.getScript().challenge2Intro()

        elif self._game.getChallengeNum() == 3:
            #get monster for the round
            self._monster = self._game.getChallenge3Monster()
            #set strength used for this round
            heroAttribute = self._hero.getStamina()
            aiAttribute = self._ai.getStamina()
            heroAttributeName = "Stamina"
            aiAttributeName = "Stamina"
            #Introduce challenge
            self._game.getScript().challenge3Intro()

        elif self._game.getChallengeNum() == 4:
            #get monster for the round
            self._monster = self._game.getChallenge4Monster()
            #set strength used for this round
            heroAttribute = self._hero.getStamina()
            aiAttribute = self._ai.getStamina()
            heroAttributeName = "Stamina"
            aiAttributeName = "Stamina"
            #Introduce challenge
            self._game.getScript().challenge4Intro()

        elif self._game.getChallengeNum() == 5:
            #get monster for the round
            self._monster = self._game.getChallenge5Monster()
            #set strength used for this round
            heroAttribute = self._hero.getStrength()
            aiAttribute = self._ai.getIntelligence()
            heroAttributeName = "Strength"
            aiAttributeName = "Intelligence"
            #Introduce challenge
            self._game.getScript().challenge5Intro()

        while not self._game.getRoundWinner():

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

            elif self._ai.characterIsAlive() == True:
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

            elif self._hero.characterIsAlive() == True:
                #Ask user to roll for the hero
                input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")
                self._hero.rollDice()
                #Calculate the total roll of the hero 
                totalHeroRoll = self._hero.getRoll() + heroAttribute
                #Ensure total roll does not goes into negative
                totalHeroRoll = max(0, totalHeroRoll)

                #Display user what hero rolled and how outcome is affected by it's attribute
                print(f"\n{self._hero.getColorName()} \033[0mrolled {self._hero.getRoll()} modified by {self._hero.getName()} {heroAttributeName} ({heroAttribute}) is {totalHeroRoll}")
                
                #Damage given by hero
                self._damageToMonster = totalHeroRoll

            #Call appropriate method according to the damage to the monster
            if self._damageToMonster <= 16:
                self.normalAttack()
            elif self._damageToMonster > 16:
                self.criticalAttack()

            #Now it's monster's turn to attack
            self.monsterAttack()

            #Alert player if someone dies
            self._game.alertPlayerAboutCharacterDeath()

            #Check if someone won the round and start the next round
            self._game.determineRoundWinner()

            #Check if someone won the game
            self._game.determineGameWinner()

    '''This method runs when critical attack is not delt'''
    def normalAttack(self):
        self.printWhoIsAttackingMonster()

        #Update monster health after damage
        self._monster.updateHealth(self._damageToMonster)
        self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}'s\033[0m remaining health: {self._monster.getHealth()}.")

    '''This method runs when critical attack is delt'''
    def criticalAttack(self):
        #TODO: give monster ability to deal with critical attack
        self.printCriticalAttackMsg()
        pass

    '''This method runs when monster attack heroes'''
    def monsterAttack(self):
        #Get monster's Roll
        self._monster.rollDice()
        monsterRoll = self._monster.getRoll()
        
        #Ensure total roll does not goes into negative
        monsterRoll = max(0, monsterRoll)
        
        #If monster rolled more than heroes roll divided by 2 he gets the chance to attack players
        if monsterRoll > (self._hero.getRoll()/2 + self._ai.getRoll()/2) and self._monster.characterIsAlive() == True:
            #monster decides wheather to attack hero or not
            self._monster.characterDecision()
            attackHero = self._monster.getCharacterDecision()

            #monster decides wheather to attack ai or not
            self._monster.characterDecision()
            attackAi = self._monster.getCharacterDecision()

            #dividing the monster's damage between hero and ai
            self._damageToHero = monsterRoll/2
            self._damageToAi = monsterRoll/2

            #if monster decided to attack both and both are alive
            if self._hero.characterIsAlive() == True and self._ai.characterIsAlive() == True and attackHero == True and attackAi == True:
                self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}\033[0m strikes back fiercely, dealing {monsterRoll} damage to both {self._hero.getColorName()}\033[0m and {self._ai.getColorName()}\033[0m!")
                self.monsterAttackHeroAndAi()
                
            #If hero is alive a monster decide to attack hero
            elif self._hero.characterIsAlive() == True and attackHero == True:
                self.monsterAttackHero()

            #If ai is alive a monster decide to attack ai
            elif self._ai.characterIsAlive() == True and attackAi == True:
                self.monsterAttackAi()
            
            #if monster decided not to attack anyone
            elif attackAi == False and attackHero == False:
                self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}\033[0m has decided to hold back and not attack this turn.")

    def printWhoIsAttackingMonster(self):
        if self._hero.characterIsAlive() == True and self._ai.characterIsAlive() == True:
            self._game.getScript().typingEffect(f"\nTogether, {self._hero.getColorName()}\033[0m and {self._ai.getColorName()}\033[0m strike, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

        elif self._ai.characterIsAlive():
            self._game.getScript().typingEffect(f"\n{self._ai.getColorName()}\033[0m strike, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

        elif self._hero.characterIsAlive():
            self._game.getScript().typingEffect(f"\n{self._hero.getColorName()}\033[0m strike, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

    def printCriticalAttackMsg(self):
        if self._hero.characterIsAlive() == True and self._ai.characterIsAlive() == True:
            self._game.getScript().typingEffect(f"\nTogether, {self._hero.getColorName()}\033[0m and {self._ai.getColorName()}\033[0m rolled critical hit, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

        elif self._ai.characterIsAlive():
            self._game.getScript().typingEffect(f"\n{self._ai.getColorName()}\033[0m rolled critical hit, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

        elif self._hero.characterIsAlive():
            self._game.getScript().typingEffect(f"\n{self._hero.getColorName()}\033[0m rolled critical hit, dealing {self._damageToMonster} damage to {self._monster.getColorName()}\033[0m!")

    def monsterAttackHero(self):
        #print monster's decision
        self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}\033[0m has decided to attack {self._hero.getColorName()}\033[0m, dealing {self._damageToHero} damage!")
        
        #update hero health and print it 
        self._hero.updateHealth(self._damageToHero)
        self._game.getScript().typingEffect(f"\n{self._hero.getColorName()}'s\033[0m remaining health: {self._hero.getHealth()}.")

    def monsterAttackAi(self):
        #print monster's decision
        self._game.getScript().typingEffect(f"\n{self._monster.getColorName()}\033[0m has decided to attack {self._ai.getColorName()}\033[0m, dealing {self._damageToAi} damage!")
        
        #update ai health and print it
        self._ai.updateHealth(self._damageToAi)
        self._game.getScript().typingEffect(f"\n{self._ai.getColorName()}'s\033[0m remaining health: {self._ai.getHealth()}.")
 
    def monsterAttackHeroAndAi(self):
        #update hero health and print it 
        self._hero.updateHealth(self._damageToHero)
        self._game.getScript().typingEffect(f"\n{self._hero.getColorName()}'s\033[0m remaining health: {self._hero.getHealth()}.")

        #update ai health and print it
        self._ai.updateHealth(self._damageToAi)
        self._game.getScript().typingEffect(f"\n{self._ai.getColorName()}'s\033[0m remaining health: {self._ai.getHealth()}.")

