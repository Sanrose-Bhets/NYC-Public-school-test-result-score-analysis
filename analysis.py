import pandas as pd

school = pd.read_csv("schools.csv")

schooling = pd.DataFrame(school)

precentage = 800 * 0.8
#subsetting the columns
desiredcolumns = schooling[["school_name","average_math"]]
best_math_schools = desiredcolumns[desiredcolumns["average_math"]>precentage].sort_values("average_math", ascending=False)
print(best_math_schools)