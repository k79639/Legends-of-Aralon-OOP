'''Represents the game application responsible for creating and running the game'''
from game import Game #import game

class Application:
    def run():
        game = Game() #creates game object
        game.run()  #call run method in game