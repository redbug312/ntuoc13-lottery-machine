import pandas as pd


COLUMNS = {'姓名': 'NAME', '學號': 'STID', '小隊': 'TEAM', 'Instagram 帳號': 'INST'}


class Attendees():
    def init_app(self, app):
        self.df = (pd.read_csv(app.config['ATTENDEES_CSV'])
                     .reindex(COLUMNS.keys(), axis=1)
                     .rename(COLUMNS, axis=1)
                     .drop_duplicates(subset='STID')
                     .fillna({'TEAM': 0, 'INST': ''}))
        self.universe = self.df.TEAM.notnull()

    def draw(self, n=1, seed=None, prefix=None, instagram=False):
        lookup = self.lookup(prefix=prefix, instagram=instagram)
        groupby = lookup.groupby(by='TEAM')
        weights = groupby.size().values  # Index always be sorted in ascending order
        try:
            chosen = (groupby.sample(n=1, random_state=seed)
                             .sample(n=n, random_state=seed, weights=weights))
        except ValueError:
            n = min(n, lookup.shape[0])
            chosen = lookup.sample(n=n, random_state=seed)
        self.df.drop(chosen.index, inplace=True)  # Everyone chosen only once
        return chosen

    def lookup(self, card=None, prefix=None, instagram=False):
        boolmask = self.universe.copy()  # Avoid passing dataframe ref
        if card:
            boolmask &= self.df.STID.eq(card.upper())
        if prefix:
            boolmask &= self.df.STID.str.contains('^[%s]' % prefix)
        if instagram:
            boolmask &= self.df.INST.ne('')
        return self.df[boolmask]


class Instagramers():
    def init_app(self, app):
        self.df = pd.read_csv(app.config['INSTAGRAM_CSV'], header=None)

    def draw(self, n=1, seed=None):
        n = min(n, self.df.shape[0])
        return self.df[0].sample(n=n, random_state=seed)

    def lookup(self):
        return self.df[0]


db = Attendees()
ig = Instagramers()
