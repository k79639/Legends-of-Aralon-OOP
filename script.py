'''This module prints and handel the script, game messages and storyteller'''
import sys
import time

class Script:
    def __init__(self, gameInstance):
        self._game = gameInstance
        self._oriana = "\033[93mOriana:\033[0m " #creates storyteller

    '''This method creates a typing effect when printing a string of characters'''
    def typingEffect(self, text, delay=0.03):

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
        self.typingEffect("\033[0mThe air crackles with anticipation...", 0.05)
        self.typingEffect("Ancient prophecies whisper of monstrous evils returning to the land of Aralon.", 0.04)
        self.typingEffect("The kingdom holds its breath, their fate hanging by a thread.")

        #Introduce the characters
        self.typingEffect("Two brave heroes have risen to face the darkness:\n", 0.04)
        self.typingEffect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage\033[0m.")
        self.typingEffect("\nTogether they will go on this perilous journey.", 0.03)
        self.typingEffect("You will choose one hero to guide through these trials, while the other will be controlled by fate itself.\n", 0.04)

        #Display gameplay rules, win-loss criteria, and quest
        self.typingEffect("As the champions of Aralon, your quest is to confront three ancient monsters,")
        self.typingEffect("each testing a different attribute: strength, stamina, and intelligence.\n")
        self.typingEffect("The outcome of each challenge is decided by the roll of two six-sided dice (range: 2-12),\n")
        self.typingEffect("combined with the hero's attributes and abilities.")
        self.typingEffect("To win, at least one hero must survive all three challenges.")
        self.typingEffect("\033[1mIf both heroes fall, darkness will consume Aralon.\033[0m\n")

        self.typingEffect("\nWhich hero will you guide, and will you save Aralon from its fate?")
        

