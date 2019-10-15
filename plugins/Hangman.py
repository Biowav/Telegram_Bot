import listener
def start_game(self):
    self.core_game()


def core_game(self):
    guesses = 0
    letters_used = ""
    the_word = "pizza"
    progress = ["?", "?", "?", "?", "?"]

    while guesses < 6:
        guess = listener.last_listen

        if guess in the_word and guess not in letters_used:
            print
            "As it turns out, your guess was RIGHT!"
            letters_used += "," + guess
            hangman_graphic(guesses)
            print
            "Progress: " + self.progress_updater(guess, the_word, progress)
            print
            "Letter used: " + letters_used
        elif guess not in the_word and guess not in letters_used:
            guesses += 1
            print("Things aren't looking so good, that guess was WRONG!")
            letters_used += "," + guess
            hangman_graphic(guesses)
            print
            "Progress: " + "".join(progress)
            print
            "Letter used: " + letters_used
        else:
            print
            "That's the wrong letter, you wanna be out here all day?"
            print
            "Try again!"


def hangman_graphic(self, guesses):
    if guesses == 0:
        print("________      ")
        print
        ("|      |      ")
        print
        ("|             ")
        print
        ("|             ")
        print
        ("|             ")
        print
        ("|             ")
    elif guesses == 1:
        print
        ("________      ")
        print
        ("|      |      ")
        print
        ("|      0      ")
        print
        ("|             ")
        print
        ("|             ")
        print
        ("|             ")
    elif guesses == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print
        ("|             ")
    elif guesses == 3:
        print
        "________      "
        print
        "|      |      "
        print
        "|      0      "
        print
        "|     /|      "
        print
        "|             "
        print
        "|             "
    elif guesses == 4:
        """"________
        |      |
        |      0
        |     /|\
        |
        |             """
    elif guesses == 5:
        """________
        |      |
        |      0
        |     /|\
        |     /
        |             """
    else:

        """________
        |      |
        |      0
        |     /|\
        |     / \
        |             """
        "GAME OVER!"


def progress_updater( guess, the_word, progress):
    i = 0
    while i < len(the_word):
        if guess == the_word[i]:
            progress[i] = guess
            i += 1
        else:
            i += 1

    return "".join(progress)