import pandas as pd

school = pd.read_csv("schools.csv")

schooling = pd.DataFrame(school)

precentage = 800 * 0.8
best_math_schools = schooling[schooling["average_math"]>precentage]
print(best_math_schools)