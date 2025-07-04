.agg fucntion I used is different from datacamp
The code i used:
        borough_stats = df.groupby('borough').agg(
            num_schools=('total_SAT', 'count'),
            average_SAT=('total_SAT', 'mean'),
            std_SAT=('total_SAT', 'std')
        ).round(2)
inside the agg function the syntax works as 
column creation = ("column to calculate",'function to use')
SYNTAX == agg(new_column_name=('column_to_aggregate', 'aggregation_function'))