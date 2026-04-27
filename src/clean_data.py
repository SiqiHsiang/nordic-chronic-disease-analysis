import pandas as pd

NORDIC_COUNTRIES = ['Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland', 'Netherlands']

def get_nordic_both_sexes(df_diabetes, countries=NORDIC_COUNTRIES):
    """Average Men/Women, filter Nordic countries."""
    return (
        df_diabetes[df_diabetes['country'].isin(countries)]
        .groupby(['country', 'iso', 'year'], as_index=False)
        [['diabetes_prevalence', 'treatment_rate']]
        .mean()
    )

def merge_obesity(df_nordic, df_obesity):
    """Merge obesity data into Nordic diabetes dataframe."""
    return pd.merge(
        df_nordic,
        df_obesity[['country', 'year', 'obesity_prevalence']],
        on=['country', 'year'],
        how='left'
    )