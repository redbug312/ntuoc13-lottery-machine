import pandas as pd


class Attendees():
    def init_app(self, app):
        self.df = pd.read_csv(app.config['ATTENDEES_CSV']) \
            .drop_duplicates(subset='學號')
        self.teams = self.df.大隊.unique()

    def draw(self, n=1, seed=None):
        per_team = (n - 1) // len(self.teams) + 1
        # TODO ask if groupby dropna=False needed
        return self.df \
            .groupby(by='大隊') \
            .sample(n=per_team, random_state=seed) \
            .sample(n=n, random_state=seed)


db = Attendees()
