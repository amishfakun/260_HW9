import pandas as pd

filenames = ["017_large.csv", "055_large.csv", "086_large.csv", "027_large.csv", "029_large.csv", "031_large.csv"]
import pandas as pd

for file in filenames:
    # Read in the CSV file
    df = pd.read_csv(file, delimiter=',')
    
    # # Drop the duplicate rows
    # df = df.drop_duplicates()
    # Pivot the data
    df_pivot = df.pivot_table(index='date_local', columns='parameter_code', values='sample_measurement')
    df_pivot = df_pivot.reset_index()
    # Print the pivoted data
    print(df_pivot.head())
    df_pivot.to_csv(file, index=False)

    

    







    