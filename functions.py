
def read(df,str):
    import pandas as pd
    df=pd.read_csv(str)
    df.head()
    print('--'*15)
    