import pandas as pd

def remove_outliers(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    
    # Define a threshold beyond which values will be considered outliers
    cutoff = threshold * std

    lower, upper = mean - cutoff, mean + cutoff
    outliers = [x for x in df[column] if x < lower or x > upper]
    df = df[(df[column] > lower) & (df[column] < upper)]
    return pd.DataFrame(df)


