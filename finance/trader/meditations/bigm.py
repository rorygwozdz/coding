"""This is simple. Asks about a random passage from meditations."""
import json
import random
import pandas as pd


class bigm:
    """Bigm (Marcus Aurelius) speaks to you. Records response."""

    def __init__(self, json_path, csv_path):
        """Intializes. big m class."""
        self.csv_path = csv_path
        with open(json_path, 'r') as file:
            self.passages = json.load(file)

    def v(self):
        """Virtue."""
        store = pd.read_csv(self.csv_path)
        book = random.choice(list(self.passages.keys()))
        passage = random.choice(self.passages[book])
        print("Here's a passage:")
        print(passage)
        print("What're your thoughts?")
        thoughts = input()
        if passage in list(store['Passage']):
            store.loc[passage, 'Thoughts'] =\
                str(store.loc[passage, 'Thoughts']) + \
                '|' + \
                thoughts
        else:
            store.append({'Passage': passage}, ignore_index=True)
            store.loc[passage, 'Thoughts'] = thoughts
        store.to_csv(self.csv_path)
