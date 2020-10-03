import pandas as pd

from faker import Faker
fake = Faker()

df = pd.read_csv("/work/testdata.csv")
orig = df.copy()

df['_Name'] = df.apply(lambda row: fake.name(), axis=1)
df['_SSN'] = df.apply(lambda row: fake.ssn(), axis=1)
df['_DOB'] = df.apply(lambda row: fake.date(), axis=1)

df.drop(['Name', 'DOB', 'SSN'], axis=1)

df.head()
