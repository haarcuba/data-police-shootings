import pandas as pd
import datetime
import IPython


def v1():
    shootings = pd.read_csv('v1/fatal-police-shootings-data.csv')
    gun=shootings['armed']=='gun'
    unarmed=shootings['armed']=='unarmed'
    unarmed_shootinge_race_counts = shootings[unarmed]['race'].value_counts()
    total_shootings = shootings.count()['id']
    earliest, latest = shootings['date'][0], shootings['date'][total_shootings-1]
    earliest = datetime.date.fromisoformat(earliest)
    latest = datetime.date.fromisoformat(latest)
    total_days = (latest - earliest).days
    total_years = total_days / 365
    unarmed_shootinge_race_counts_per_year = unarmed_shootinge_race_counts / total_years

    IPython.embed()


if __name__ == '__main__':
    v1()
