import pandas as pd

school = pd.read_csv("schools.csv")

schooling = pd.DataFrame(school)

print(schooling.head())