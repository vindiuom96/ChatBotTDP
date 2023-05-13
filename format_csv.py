import pandas as pd

df1 = pd.read_csv("CSV/entities_exported.csv")
print(df1['/name'])
def format_csv():
    global df1
    df2 = df1[df1['/name'].isna()]
    df1 = df1.drop(df2.index.tolist())
    df2 = df1[df1['/acceptedAnswer/text'].isna()]
    df1 = df1.drop(df2.index.tolist())
    print(df1['/name'])
    return df1
