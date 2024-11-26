'''This module handels the logic of all the challenges in the game'''

class Challenge:
    def __init__(self, gameInstance):
        self._game = gameInstance

    def battlefield(self):
        hero = self._game.getHero()
        ai = self._game.getAi()
        if self._game.getChallengeNum() == 1:
            #get monster for the round
            monster = self._game.getChallenge1Monster()
            #set strength used for this round
            heroAttribute = hero.getStrength()
            aiAttribute = ai.getStrength()
            heroAttributeName = "Strength"
            aiAttributeName = "Strength"
            #Introduce challenge and Oriana
            self._game.getScript().orianaAndChallenge1Intro()
            #Dialogues for the first challenge
            self._game.getScript().challenge1Dialogues()

        #Loop round until either one of the character or Monster wins the game
        while monster.getHealth() > 0 and (hero.getHealth() > 0 or ai.getHealth() > 0):
            #Get monster's Roll
            monster.rollDice()
            monsterRoll = monster.getRoll()

            #Check if both hero can roll for the round
            if hero.characterIsAlive() == True and ai.characterIsAlive() == True:

                #Ask user to roll for the hero
                input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")
                hero.rollDice()
                #Calculate the total roll of the hero 
                totalHeroRoll = hero.getRoll() + heroAttribute
                #Ensure total roll does not goes into negative
                totalHeroRoll = max(0, totalHeroRoll)

                #AI rolls on its turn.
                ai.rollDice()
                #Calculate the total roll of the Ai 
                totalAiRoll = ai.getRoll() + aiAttribute
                #Ensure total roll does not goes into negative
                totalAiRoll = max(0, totalAiRoll)

                #Display user what each character rolled and how outcome is affected by their attribute
                print(f"\n{hero.getColorName()} \033[0mrolled {hero.getRoll()} modified by {hero.getName()} {heroAttributeName} ({heroAttribute}) is {totalHeroRoll}")
                print(f"\n{ai.getColorName()} \033[0mrolled {ai.getRoll()} modified by {ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")

                #Calclate the total damage from both heroes
                combinedDamage = totalHeroRoll + totalAiRoll

            elif ai.characterIsAlive():
                #AI rolls on its turn.
                ai.rollDice()
                #Calculate the total roll of the Ai 
                totalAiRoll = ai.getRoll() + aiAttribute
                #Ensure total roll does not goes into negative
                totalAiRoll = max(0, totalAiRoll)

                #Display user what Ai rolled and how outcome is affected by it's attribute
                print(f"\n{ai.getColorName()} \033[0mrolled {ai.getRoll()} modified by {ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")


            elif hero.characterIsAlive():
                #Ask user to roll for the hero
                input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")
                hero.rollDice()
                #Calculate the total roll of the hero 
                totalHeroRoll = hero.getRoll() + heroAttribute
                #Ensure total roll does not goes into negative
                totalHeroRoll = max(0, totalHeroRoll)

                #Display user what Ai rolled and how outcome is affected by it's attribute
                print(f"\n{ai.getColorName()} \033[0mrolled {ai.getRoll()} modified by {ai.getName()} {aiAttributeName} ({aiAttribute}) is {totalAiRoll}")

