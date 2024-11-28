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



        

