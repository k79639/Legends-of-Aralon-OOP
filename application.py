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
        # script.displayWelcome()

        #Prints the characters options to choose from
        # script.displayOptions()

        
        #Allow the user to choose one of the two roles implemented in the game and handel errors
        validChoice = False
        while not validChoice:
            userChoice = self.selectCharacter()  #Prompt the user to select a character
            
            # Handle None returned by selectCharacter (interrupted or invalid)
            if userChoice is None:  
                continueChoice = input("\nType \033[1m'Y'\033[0m to continue, or press Enter to exit the game: ").strip().lower()
                
                if len(continueChoice) == 0:  #user pressed Enter to exit
                    print("\nExiting the game. Goodbye!")
                    break
                elif continueChoice == "y":  #User chooses to continue
                    continue
                else:  #Invalid input
                    print("\n\033[91mInvalid input.\033[0m Exiting the game.")
                    break
            else:  #valid character selection
                validChoice = True
                game.createCharacters(userChoice)  # Create the selected character
                game.run()  # Start the game
    
    '''This method allow user to select one of the two characters implemented in the game'''
    def selectCharacter(self):
        breakLoop = False
        while not breakLoop: #Loop until user gives valid choice
            try:
                #strip the space from front and back of the user input (if added) and convert it into lowercase
                selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower() 
                if selectedHero == "valerius" or selectedHero == "v":
                    breakLoop = True
                    return "Valerius"

                elif selectedHero == "eldara" or selectedHero == "e":
                    breakLoop = True
                    return "Eldara"
                else:
                    print("\n\033[91mInvalid choice.\033[0m Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.")
            #catch keyboard interruption error
            except KeyboardInterrupt:
                breakLoop = True
                print("\n\t\033[91mInput interrupted.\033[0m")

