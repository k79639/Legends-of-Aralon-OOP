'''Represents the game application responsible for creating and running the game'''
from game import Game #import game
from script import Script

class Application:
    def run(self):
        
        game = Game() #creates game object

        #Create script and pass game instance to script
        script = Script(game)

        # pass script instance to game
        game.setScript(script)

        #Print a “welcome” message and provide a short overview of the game
        script.displayWelcome()

        #Prints the characters options to choose from
        script.displayOptions()

        #Allow the user to choose one of the two roles implemented in the game
        userChoice = self.selectCharacter()

        #Give user choice to game to create character and start the game
        game.createCharacters(userChoice)

        game.run()  #call run method of game
    
    '''This method allow user to select one of the two characters implemented in the game'''
    def selectCharacter(self):
        validChoice = False
        while not validChoice: #Loop until user gives valid choice
            global selectedHero
            #strip the space from front and back of the user input (if added) and convert it into lowercase
            selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower() 
            if selectedHero == "valerius":
                validChoice = True
                return "Valerius"

            elif selectedHero == "eldara":
                validChoice = True
                return "Eldara"

            else:
                print("\n\033[91mInvalid choice.\033[0m Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.")