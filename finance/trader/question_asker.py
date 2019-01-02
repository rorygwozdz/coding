"""Game for asking questions."""
import pandas as pd


class qs:
    """The engine for the questions.

    needs acess to a to a csv of questions
    ran from trader
    """

    def __init__(self, filepath, rounds):
        """intializes."""
        self.rounds = int(rounds)
        self.filepath = filepath
        print(filepath)
        print('derka')
        self.all_questions = pd.read_csv(filepath, encoding='latin1')

    def play(self):
        """Game runner. Saves and updates."""
        aqs = self.all_questions
        unanswered = aqs[aqs['Answer'].isnull()]
        assert len(unanswered) > self.rounds, "Not enough new questions. \
        Hotfix: Wipe the questions and restart."
        qs = unanswered.sample(self.rounds)
        for i in qs.index:
            print(qs.loc[i, 'Question'])
            qs.loc[i, ['Answer']] = input()
        aqs.update(qs)
        aqs.to_csv(self.filepath, index=False)
