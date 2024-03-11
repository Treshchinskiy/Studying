
def read(df,str):
    import pandas as pd
    df=pd.read_csv(str)
    df.head()
    print('--'*15)
    



def print_report(y_pred,y_test):
    from sklearn.metrics import classification_report
    print(classification_report(y_pred,y_test))