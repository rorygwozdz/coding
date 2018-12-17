import numpy as np


class math_test:
    def __init__(self, rounds=5):
        self.rounds = rounds
        self.times_wrong = 0
        self.answer = 0
        self.answer_actual = 0
        # different types of games
        self.multipliers = np.arange(1, 200)
        self.adders = np.arange(100, 1000, 1)
        self.adders_options = np.arange(-5, 5, .05)
        self.modes = np.arange(2)

    def play(self):  # returns number wrong
    """Plays the game.

    The core of the mental math script, this is focuses
    on playing the version you wanted, and returning
    an answer based on thatself."""
        for i in range(self.rounds):
            self.mode = np.random.choice(self.modes)
            if self.mode == 0:
                self.multiplication()
            elif self.mode == 1:
                self.add()
            elif self.mode == 2:
                self.add_options()
                # TODO: make the options version with -o
            if self.answer == 'quit':
                return self.quit()
            if self.answer == self.answer_actual:
                print("You got it!")
            elif float(self.answer) == self.answer_actual:
                print("You got it!")
            elif self.answer == 'quit':
                return self.quit()
            else:
                self.times_wrong += 1
                print("Not quite. The answer was %s." % self.answer_actual)
        if self.times_wrong == 0:
            print("You're a literal rockstar. You got em' all right.")
        else:
            print("It's okay. You got %s wrong out of %s problems." %
                  (self.times_wrong, self.rounds))
        return self.times_wrong

    def multiplication(self):
        """Plays multiplication version. Asks question and grabs answer."""
        decill = np.round(np.random.choice(self.multipliers/100), 3)
        intrr = np.round(np.random.choice(self.multipliers))
        self.answer_actual = np.round(decill*intrr, 3)
        print("What is %s percent of %s?" % (int(round(decill * 100)), intrr))
        self.answer = input()
        self.answer = str(float(self.answer))

    def add(self):
        """Plays adding game. Ask questions, takes answers."""
        first_num = np.random.choice(self.adders)
        second_num = np.random.choice(self.adders)
        self.answer_actual = np.round(first_num + second_num, 3)
        print("What's %s plus %s?" % (first_num, second_num))
        self.answer = input()
        self.answer = str(int(self.answer))

    def add_options(self):
        """Switches to option adding."""
        first_num = np.random.choice(self.adders_options)
        second_num = np.random.choice(self.adders_options)
        self.answer_actual = np.round(first_num + second_num, 3)
        print("What's %s plus %s?" % (first_num, second_num))
        self.answer = input()
        self.answer = str(int(self.answer))

    def quit(self):
        """Quits out of the game, if 'quit' was the answer."""
        quit = True
        assert quit is not True, 'You said you wanted to quit, \
               and now here we are.'
