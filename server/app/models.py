import pandas as pd


COLUMNS = ['姓名', '學號', '大隊']


class Attendees():
    def init_app(self, app):
        self.df = pd.read_csv(app.config['ATTENDEES_CSV']) \
            .filter(items=COLUMNS) \
            .drop_duplicates(subset='學號') \
            .fillna({'大隊': 0})  # Avoid handle NaN after leftjoin
        self.teams = self.df.大隊.unique()

    def draw(self, n=1, seed=None, prefix='BRD'):
        boolmask = self.df.學號.str.contains(f'^[{prefix}]')
        groupby = self.df.loc[boolmask].groupby(by='大隊')
        weights = groupby.size().values  # Index always be sorted in ascending order
        return groupby \
            .sample(n=1, random_state=seed) \
            .sample(n=n, random_state=seed, weights=weights)

    def lookup(self, card=None):
        return self.df[self.df.學號 == card.upper()] if card \
            else self.df  # Dump all attendees


db = Attendees()
