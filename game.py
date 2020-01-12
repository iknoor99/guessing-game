
class game:

    """
    Class game for storing the results for a specific user playing a number of games.
    """

    gamenum = 0
    gamelist = []

    frequency_dict = {

        "a": 8.17,
        "b": 1.49,
        "c": 2.78,
        "d": 4.25,
        "e": 12.70,
        "f": 2.23,
        "g": 2.02,
        "h": 6.09,
        "i": 6.97,
        "j": 0.15,
        "k": 0.77,
        "l": 4.03,
        "m": 2.41,
        "n": 6.75,
        "o": 7.51,
        "p": 1.93,
        "q": 0.10,
        "r": 5.99,
        "s": 6.33,
        "t": 9.06,
        "u": 2.76,
        "v": 0.98,
        "w": 2.36,
        "x": 0.15,
        "y": 1.97,
        "z": 0.07

    }

    def __init__(self):

        """
        Constructor for defining the instance attributes like gamenum, word, status, bad guess ,
        missed letters and the score for each game which will be stored eventually in a list

        """

        game.gamenum = game.gamenum + 1
        self.word = ""
        self.status = ""
        self.bad_guess = 0
        self.missed_letters = 0
        self.score = 0

    @classmethod
    def display_play(cls):

        """
        Method for displaying the final table of the number of games and corresponding statistics with
        the final score
        """

        print("{:4s} {:4s} {:7s} {:11s} {:14s} {:5s}".format('Game', 'Word', 'status', 'Bad Guesses', 'Missed Letters',

                                                           'Score'))

        print("{:4s} {:4s} {:7s} {:11s} {:14s} {:5s}".format('----', '----', '-------', '-----------', '--------------',

                                                           '------'))

        finalscore=0
        for i in game.gamelist:

                print(
                    "{:<4d} {:>4s} {:>7s} {:<11d} {:<14d} {:<0.2f}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

                finalscore = finalscore + i[5]

        print()
        print("Final Score :" + "{:.2f}".format(finalscore))



    def check_word(self, lastvalue, actualstring, bad_guessnum,lettertimes,missedlet):

        """
        Method for calculating the score of the word guessed correctly by considering the
        number of bad guesses, total numnber of letter guess as well as no. of wrong letter guesses

        """

        self.word = actualstring
        self.status = "success"
        self.bad_guess = bad_guessnum
        self.missed_letters = missedlet
        self.lettertimes = lettertimes

        score = 0

        for i in range(0, len(lastvalue)):
            if (lastvalue[i] == '-'):

                value = actualstring[i]
                print()
                score = score + game.frequency_dict.get(value)

        if(self.bad_guess != 0):

            score = score-(0.1*score*self.bad_guess)

        if(self.lettertimes!=0):
            score = score / lettertimes

        self.score = score

        indgamelist = [game.gamenum, self.word, self.status, self.bad_guess, self.missed_letters, self.score]

        game.gamelist.append(indgamelist)


    def check_giveup(self, lastvalue,actualstring,bad_guessnum,missedlet):

        """
        Method for calculating the score of the word for which the user "gave up" by considering the
        number of bad guesses, total numnber of letter guess as well as no. of wrong letter guesses

        """

        self.word = actualstring
        self.status = "Gave up"
        self.bad_guess = bad_guessnum
        self.missed_letters = missedlet

        score = 0

        for i in range(0, len(lastvalue)):
            if (lastvalue[i] == '-'):

                value = actualstring[i]
                score = score + game.frequency_dict.get(value)

        self.score = -score

        indgamelist = [game.gamenum, self.word, self.status, self.bad_guess, self.missed_letters, self.score]

        game.gamelist.append(indgamelist)

    def check_quit(self):

        game.display_play()
