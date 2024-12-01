'''Creates and runs the application. This is the starting module of the program.'''
from application import Application
import sys

try:
    app = Application() #creates application object

    app.run() #call run method in application

#Catch and handel keyboard interruption
except KeyboardInterrupt:
    print("")
    print("\n\t\033[91mInput interrupted.\033[0m Exiting the game.")
    print("")
    sys.exit(0)

except Exception as ex:
    print(f"\nAn unexpected error ocurred in the program. Please try again or contact your administration.\nError Message: {ex}")