def columns_values(dataframe):
    for n in dataframe.columns:                               # cycle through the columns in dataframe
        column = n  
        value_counts = (dataframe[column].value_counts())     # run value counts for each column
        unique_values = (dataframe[column].unique())          # run unique values for each column 
        len_counts = len(value_counts)                        # how many items are counted in value counts
        len_unique = len(unique_values)                       # how many items are counted in unique values
        if (len(value_counts)< 100):                          # ignore columns where counts over 100
                print(f"{column} has length of {len_unique}") # print how many unique values there are
                print(unique_values)                          # print unique values for column 
                print("="*30)                                  
                print(f"{column} has length of {len_counts}") # print how many values are counted
                print(value_counts)                           # print unique values counted
                print("="*60)
