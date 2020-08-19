import pandas as pd


COLUMNS = ['姓名', '學號', '大隊']


class Attendees():
    def init_app(self, app):
        self.df = pd.read_csv(app.config['ATTENDEES_CSV']) \
            .reindex(COLUMNS, axis=1) \
            .drop_duplicates(subset='學號') \
            .fillna({'大隊': 0})  # Avoid handle NaN after leftjoin
        self.universe = self.df.大隊.notnull()
        self.teams = self.df.大隊.unique()

    def draw(self, n=1, seed=None, prefix=None):
        lookup = self.lookup(prefix=prefix)
        groupby = lookup.groupby(by='大隊')
        weights = groupby.size().values  # Index always be sorted in ascending order
        try:
            return groupby.sample(n=1, random_state=seed) \
                          .sample(n=n, random_state=seed, weights=weights)
        except ValueError:
            n = min(n, lookup.shape[0])
            return lookup.sample(n=n, random_state=seed)

    def lookup(self, card=None, prefix=None):
        boolmask = self.universe
        boolmask = boolmask & \
            (self.df.學號.str.contains(f'^[{prefix}]') if prefix
             else self.universe)
        boolmask = boolmask & \
            (self.df.學號 == card.upper() if card
             else self.universe)
        return self.df[boolmask]


db = Attendees()
