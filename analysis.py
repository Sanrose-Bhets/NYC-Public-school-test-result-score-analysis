import pandas as pd

school = pd.read_csv("schools.csv")

schooling = pd.DataFrame(school)

# Best maths Results Calculations
precentage = 800 * 0.8
# Slicing/subsetting desired columns to make the below code much more understanding
desiredcolumns = schooling[["school_name", "average_math"]]
best_math_schools = desiredcolumns[desiredcolumns["average_math"] > precentage].sort_values("average_math", ascending=False)
print(best_math_schools)

# Top 10 performing schooling in SATs
schooling["total_SAT"] = schooling["average_math"] + schooling["average_reading"] + schooling["average_writing"]

top_SAT = schooling.sort_values("total_SAT", ascending=False)
columnsdesired = top_SAT[["school_name", "total_SAT"]]
top_10_schools = columnsdesired.iloc[0:10, :]
print(top_10_schools)

# Calculating the Standard Deviation of all the schools Numeric Values
stats_borrowed = schooling.groupby("borough").agg(
    num_schools=('total_SAT', 'count'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
).round(2).sort_values("std_SAT", ascending=False)

largest_std_dev = stats_borrowed.iloc[0]

print(largest_std_dev)