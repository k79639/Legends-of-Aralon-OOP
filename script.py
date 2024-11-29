'''This module prints and handel the script, game messages and storyteller'''
import sys
import time

class Script:
    def __init__(self, gameInstance):
        self._game = gameInstance
        self._oriana = "\033[93mOriana:\033[0m " #Define storyteller
        self._ai = None
        self._hero = None

    '''This method creates a typing effect when printing a string of characters'''
    def typingEffect(self, text, delay=0.00):

        for char in text: #Loop through each character in the input text
            sys.stdout.write(char) #Write the character without a new line
            sys.stdout.flush() #Force the output to appear immediately 
            time.sleep(delay) #Pause for specific delay
        print() #Prints the characters

    '''This method displays the welcome message game rules and overview of the story'''
    def displayWelcome(self):
        #Prints the game title
        print("\n" + "\033[7m-" * 8 +" Legends of Aralon "+"-" * 8 +"\033[0m\n")

        #Prints the background story
        # self.typingEffect("\033[0mThe air crackles with anticipation...", 0.05)
        # self.typingEffect("Ancient prophecies whisper of monstrous evils returning to the land of Aralon.", 0.04)
        self.typingEffect("The kingdom holds its breath, their fate hanging by a thread.")

        #Introduce the characters
        # self.typingEffect("Two brave heroes have risen to face the darkness:\n", 0.04)
        self.typingEffect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage\033[0m.")
        # self.typingEffect("\nTogether they will go on this perilous journey.", 0.03)
        # self.typingEffect("You will choose one hero to guide through these trials, while the other will be controlled by fate itself.\n", 0.04)

        #Display gameplay rules, win-loss criteria, and quest
        self.typingEffect("As the champions of Aralon, your quest is to confront three ancient monsters,")
        self.typingEffect("each testing a different attribute: strength, stamina, and intelligence.\n")
        self.typingEffect("The outcome of each challenge is decided by the roll of two six-sided dice (range: 2-12),\n")
        self.typingEffect("combined with the hero's attributes and abilities.")
        self.typingEffect("To win, at least one hero must survive all three challenges.")
        self.typingEffect("\033[1mIf both heroes fall, darkness will consume Aralon.\033[0m\n")

        self.typingEffect("Which hero will you guide, and will you save Aralon from its fate?\n")

    '''show the two characters options to choose from'''
    def displayOptions(self):
        #Display the options
        self.typingEffect("\nWill you take up the mantle of")
        self.typingEffect("\033[92mValerius, the Guardian Knight,\033[0m")
        self.typingEffect("or embrace the mystical path of")
        self.typingEffect("\033[94mEldara, the Mystic Sage?")

        #Display characters attributes
        self.typingEffect("\n\033[92mValerius, the Guardian Knight,\033[0m")
        self.typingEffect("- Stamina: +2\n- Strength: +2\n- wisdom: -3\n- Health: 50")
        self.typingEffect("- Special Abilities: Can break a monster's shield once and restore 40% of health twice.")
        self.typingEffect("\n\033[94mEldara, the Mystic Sage:\033[0m")
        self.typingEffect("- Stamina: -1\n- Strength: -2\n- Intelligence: +3\n- Health: 50")
        self.typingEffect("- Special Ability: Can dodge a monster's attack twice and respawn with 65% of health once.\n")
        self.typingEffect("Type \033[92m'Valerius'\033[0m to embody strength and resilience,")
        self.typingEffect("or \033[94m'Eldara'\033[0m to wield the power of wisdom and magic.")

    '''This method displays the roles assigned to the characters and assign them to variables hero and ai'''
    def displayRoles(self):
        #assign hero and ai to hero and ai field variable
        self._hero = self._game.getHero()
        self._ai = self._game.getAi()
        
        self.typingEffect(f"\nYou have chosen {self._hero.getColorName()}, {self._hero.getTitle()}\033[0m")
        self.typingEffect(f"The character assigned to AI is {self._ai.getColorName()}, {self._ai.getTitle()}\033[0m Prepare for battle!\n")

    '''This method introduces the storyteller and first challenge'''
    def orianaAndChallenge1Intro(self):
        self.typingEffect(f"\n{self._oriana}Greetings, hero. I am Oriana, chronicler of Aralon.")
        self.typingEffect("        Prepare yourself for the first challenge: \033[35mKragnar the Stoneborn\033[0m.")
        self.typingEffect("        A towering beast of immense strength who can summon a shield to block critical attacks.")
        self.typingEffect("        Strike wisely, for strategy and strength will decide this battle.\n")

    '''This method prints the dialogues before challenge 1'''
    def challenge1Dialogues(self):
        self.typingEffect("\033[35mKragnar: \033[0mYou both, daring to challenge me?")
        self.typingEffect("         You must be brave or foolish to face the Stoneborn.\n")

        # Hero's response
        self.typingEffect(f"{self._hero.getColorName()}: \033[0mYou may be strong, but every stone can be shattered with enough will!")
        
        # AI response
        self.typingEffect(f"\n\033[94m{self._ai.getColorName()}: \033[0mI'll strike with precision, and you'll fall before me.\n")
        self.typingEffect("\033[35mKragnar: \033[0mEnough talk! Prepare to meet your end, heroes!\n")
    
    '''This method introduces challenge 2'''
    def challenge2Intro(self):
        self.typingEffect(f"\n{self._oriana}Heroes, your next trial awaits in the dark forests where no light reaches.\n")
        self.typingEffect("        There lurks \033[35mAzra, the Mirror Fiend\033[0m, a creature of cunning and deception.")
        self.typingEffect("        \033[31mBeware,\033[0m for Azra can reflect your attacks, turning your strength against you.\n")
        self.typingEffect("        Work together, heroes. Only strategy and unity will lead to victory.\n")

    '''This method introduces challenge 3'''
    def challenge3Intro(self):
        self.typingEffect(f"\n{self._oriana}You have come far, but a greater threat awaits.\n")
        self.typingEffect("        Beneath the scorched lands lies \033[35mMalakar, the Life Leech\033[0m.")
        self.typingEffect("        His hunger is endless, draining strength with every strike.\n")
        self.typingEffect("        \033[31mBeware:\033[0m The more he attacks, the stronger he becomes.\n")
        self.typingEffect("        Only endurance and resolve can bring you victory.\n")

    '''This method introduces challenge 4'''
    def challenge4Intro(self):
        self.typingEffect(f"\n{self._oriana}You have overcome \033[35mMalakar, the Life Leech\033[0m, but the greatest danger lies ahead.\n")
        self.typingEffect("        Deep within the fiery heart of the mountain awaits \033[35mIgnarok, the Blazing Drake\033[0m.")
        self.typingEffect("        Its flames burn hotter than the sun and can turn even the bravest to ash.\n")
        self.typingEffect("        \033[31mBe warned:\033[0m When \033[35mIgnarok\033[0m falls, it will erupt in a fiery explosion, dealing deadly damage.")
        self.typingEffect("        Stay vigilant, for Ignarok's flames are as unpredictable as they are fierce.\n")
        self.typingEffect("        Only endurance and resolve will see you through this final trial.\n")

    '''This method introduces challenge 5'''
    def challenge5Intro(self):
        self.typingEffect(f"\n{self._oriana}This is it, heroes. The final battle awaits.\n")
        self.typingEffect("        In the heart of the ancient ruins, \033[35mZarok, the Deathbringer\033[0m awaits.")
        self.typingEffect("        \033[35mZarok\033[0m wields the power to drain life, leaving only darkness in his wake.\n")
        self.typingEffect("        \033[31mBeware:\033[0m When \033[35mZarok\033[0m's health drops below 16, his power doubles.\n")
        self.typingEffect("        Defeat Zarok, and Aralon will be free. Fail, and the light will fade forever.\n")

    '''Zaroks final dialogues when he looses'''
    def zarokFinalDialogues(self):
        self.typingEffect(f"\n\033[35mZarok\033[0m: \033[0mImpossible... How could I be defeated by mere mortals?")
        self.typingEffect("       My power fades... and I am vanquished, hero.")
        self.typingEffect("       The darkness recedes, but shadows will always remain in the hearts of men.\n")
        self.typingEffect("       My reign is over. Enjoy your victory, for it is fleeting.")

    '''Oriana's final dialogues'''
    def orianaFinalDialogues(self):
        self.typingEffect(f"\n{self._oriana}You did it! Zarok is defeated, and Aralon is saved.")
        self.typingEffect("        Your bravery has restored light to the kingdom.\n")
        self.typingEffect("        \033[1mRest now, champions. Your tale will be sung for generations.\033[0m")

    '''Thank you message for the player'''
    def thankyouMessage(self):
        self.typingEffect("\n\033[7mThank you for playing Legends of Aralon.\033[7m\n", 0.04)




    




        

