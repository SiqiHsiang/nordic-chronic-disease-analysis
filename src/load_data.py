import pandas as pd

DIABETES_COLS = {
    'Country/Region/World': 'country',
    'ISO': 'iso',
    'Sex': 'sex',
    'Year': 'year',
    'Age': 'age',
    'Prevalence of diabetes (18+ years)': 'diabetes_prevalence',
    'Prevalence of diabetes (18+ years) lower 95% uncertainty interval': 'diabetes_lower_ci',
    'Prevalence of diabetes (18+ years) upper 95% uncertainty interval': 'diabetes_upper_ci',
    'Proportion of people with diabetes who were treated (30+ years)': 'treatment_rate',
    'Proportion of people with diabetes who were treated (30+ years) lower 95% uncertainty interval': 'treatment_lower_ci',
    'Proportion of people with diabetes who were treated (30+ years) upper 95% uncertainty interval': 'treatment_upper_ci'
}

OBESITY_COLS = {
    'Entity': 'country',
    'Code': 'iso',
    'Year': 'year',
    'Prevalence of obesity among adults, BMI >= 30 (crude estimate) (%) - Sex: both sexes - Age group: 18+  years of age': 'obesity_prevalence'
}

def load_diabetes(path='../data/diabetes.csv'):
    df = pd.read_csv(path)
    return df.rename(columns=DIABETES_COLS)

def load_obesity(path='../data/obesity.csv'):
    df = pd.read_csv(path)
    return df.rename(columns=OBESITY_COLS)