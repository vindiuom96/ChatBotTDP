import pandas as pd

def format_csv():
    df1 = pd.read_csv("CSV/entities_exported.csv")
    df2 = df1[df1['/name'].isna()]
    df1 = df1.drop(df2.index.tolist())
    df2 = df1[df1['/acceptedAnswer/text'].isna()]
    df1 = df1.drop(df2.index.tolist())
    return df1
