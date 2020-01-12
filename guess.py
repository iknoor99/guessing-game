import stringDatabase
import game


class guess:

    """
    The game starts here ,the class guess for starting the game
    """

    def menu(self):
        """
        Function displaying the Menu and determing the course of action for playing the game
        """
        print("** The great guessing game **")
        print()
        print("Current Guess: ----")
        print()

        flag2 = True

        while (flag2):

            flag1 = True

            choosen_string = stringDatabase.stringDatabase().populate_data()
            choosen_string.lower()

            print(choosen_string)
            letter_count = 0
            guessincorct_count = 0
            letterincorct_count = 0

            indexlist = ['-', '-', '-', '-']
            displaylist = ['-', '-', '-', '-']

            final = "".join(indexlist)

            while (flag1):

                print("g = guess, t = tell me, l for a letter, and q to quit \n")
                option = input()

                if option.lower() == 'l':

                    """ 
                    If the option letter is choosen 
                    """
                    let = input("Enter a letter:\n").lower()

                    if (len(let) == 1):

                        if(let not in final):

                            letcount = choosen_string.count(let)
                            letter_count = letter_count + 1

                            if (letcount > 0):

                                print("You found " + str(letcount) + " letters")

                                if '-' in displaylist:
                                    for i in range(0, len(choosen_string)):
                                        if (choosen_string[i] == let.lower()):
                                            displaylist[i] = let

                                if (indexlist.count("-") == letcount):

                                    game.game().check_word("".join(indexlist), choosen_string, guessincorct_count,
                                                           letter_count, letterincorct_count)


                                    print("Correct you won ,Genius")
                                    print("The word is "+ "".join(displaylist))
                                    print("Next game--------------")
                                    flag1 = False

                                else:
                                    for i in range(0, len(choosen_string)):
                                        if (choosen_string[i] == let.lower()):
                                            indexlist[i] = let

                                    final = "".join(indexlist)
                                    print("Current Guess: " + final)

                            else:

                                letterincorct_count += 1
                                print("This letter does not exist,Try again!")
                                print("Current Guess: " + final)

                        else:

                            print("This letter is already included ,Try again!")
                            print("Current Guess: " + final)

                    else:

                        print("Please enter a valid letter, Try again!")
                        print("Current Guess: " + final)

                elif option.lower() == 'g':

                    """ 
                    If the option guess word is choosen 
                    """

                    fullguess = input("Enter the word \n").lower()

                    if (choosen_string != fullguess):

                        guessincorct_count = guessincorct_count + 1
                        print("Try again!,Loser")
                        print("Current Guess: " + final)

                    else:

                        print("Correct you won ,Genius")
                        print("The word is "+ fullguess)
                        game.game().check_word(final, choosen_string, guessincorct_count, letter_count, letterincorct_count)
                        print("Next game--------------")
                        flag1 = False

                elif option.lower() == 't':

                    """ 
                    If the option tell me is choosen 
                    """

                    print("Correct word is:" + choosen_string)
                    game.game().check_giveup(final, choosen_string, guessincorct_count, letterincorct_count)
                    print("Next game--------------")
                    flag1 = False

                elif option.lower() == 'q':

                    """ 
                    If the option quit is choosen 
                    """

                    game.game().check_quit()

                    flag1 = False
                    flag2 = False

                else:
                    print("Try again! Please enter the correct menu option")


guess().menu()
