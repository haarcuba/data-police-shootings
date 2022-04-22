import pandas as pd
import IPython


def main():
    shootings = pd.read_csv('fatal-police-shootings-data.csv')
    gun=shootings['armed']=='gun'
    unarmed=shootings['armed']=='unarmed'
    unarmed_shootinge_race_counts = shootings[unarmed]['race'].value_counts()
    YEARS = 2022 - 2015
    unarmed_shootinge_race_counts_per_year = unarmed_shootinge_race_counts / YEARS

    IPython.embed()


if __name__ == '__main__':
    main()
