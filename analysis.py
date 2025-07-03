import pandas as pd

school = pd.read_csv("schools.csv")

schooling = pd.DataFrame(school)

precentage = 800 * 0.8
#subsetting the columns
#Best maths Results Calculations
precentage = 800 * 0.8
desiredcolumns = schooling[["school_name","average_math"]]
best_math_schools = desiredcolumns[desiredcolumns["average_math"]>precentage].sort_values("average_math", ascending=False)
print(best_math_schools)

#Top 10 performing schooling in SATs
schooling["total_SAT"] = schooling["average_math"] + schooling["average_reading"] + schooling["average_writing"]


top_SAT=schooling.sort_values("total_SAT",ascending=False)
top_10_schools = top_SAT.iloc[0:10,:]
print(top_10_schools)