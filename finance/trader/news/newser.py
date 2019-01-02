"""This one asks about the news, bro."""
import csv


class updater:
    """This appends to a csv and keeps track of your news commentary.

    grabs datetime, products, direction, commentary, and interesting.
    """

    def __init__(self, datetime, filepath):
        """Use for setting date of play."""
        self.datetime = datetime
        self.filepath = filepath

    def play(self):
        """Intializer for the game."""
        self.product()
        self.direction()
        self.commentary()
        self.interesting()
        self.links()
        self.appender()

    def product(self):
        """Asks about today products."""
        print("I'm going to ask you about products.")
        print('What are you looking at today?')
        self.products = input()
        self.products = self.products.replace(',', '')
        self.products = self.products.replace('and', '')
        self.products = self.products.split()

    def direction(self):
        """Asks about direction of products."""
        self.d_answers = []
        print("I'm going to ask you about directionality.")
        print("Answers are bear, bull, and neutral.")
        for i in self.products:
            print("Direction on {}?".format(i))
            self.answer = input()
            self.d_answers += [self.answer]
        for i in range(len(self.d_answers)):
            if self.d_answers[i] == 'bear':
                self.d_answers[i] = -1
            elif self.d_answers[i] == 'bull':
                self.d_answers[i] = 1
            else:
                self.d_answers[i] = 0

    def commentary(self):
        """Asks for commentary on products."""
        self.c_answers = []
        print("I'm going to ask you for commentary now.")
        for i in self.products:
            print("Commentary on {}?".format(i))
            self.answer = input()
            self.c_answers += [self.answer]

    def interesting(self):
        """Asks if there's anything interesting going on."""
        print("I'm going to ask you if there's anything interesting.")
        print('Well, is there?')
        self.i_answer = input()

    def links(self):
        """Asks if there's good links."""
        print('Any good links? How many?')
        self.links = {}
        num_o_links = int(input())
        for i in range(num_o_links):
            if i > 0:
                print('Again.')
            print('Label first.')
            self.l_label = input()
            print('Now the link.')
            self.l_link = input()
            self.links[self.l_label] = self.l_link

    def appender(self):
        """Append news to our handy csv."""
        with open(self.filepath, 'a', newline='') as csver:
            f_names = [
                'Datetime',
                'Products',
                'Directions',
                'Commentary',
                'Interesting',
                'Links'
                ]
            my_dict = {
                f_names[0]: self.datetime,
                f_names[1]: self.products,
                f_names[2]: self.d_answers,
                f_names[3]: self.c_answers,
                f_names[4]: self.i_answer,
                f_names[5]: self.links
                }
            writer = csv.DictWriter(csver, fieldnames=f_names)
            # only use to make a header
            writer.writeheader()
            writer.writerow(my_dict)
