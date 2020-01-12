import random

class stringDatabase:

    """
    Class stringDatabase for I/O operations
    """

    def populate_data(self):

        """
        Function for populating the 4 letter word into a list
        and choosing a random letter everytime we play the game

        """

        with open("four_letters.txt") as file:
            dataline = file.readlines()
            lettersfinal = []
            for data in dataline:
                data = data.strip("\n")
                lettersfinal = lettersfinal + data.split(" ")


        randomletter = random.choice(lettersfinal)
        return randomletter








