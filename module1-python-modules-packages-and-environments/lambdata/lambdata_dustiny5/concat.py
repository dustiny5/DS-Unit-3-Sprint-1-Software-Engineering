#!/users/bin/env/python
'''
Input a list and change to a series. Finally concat to a new Data Frame
'''
import pandas as pd

feature = None
df = None

def concat_feature(feature, df):
    '''
    Input a list and change to a series. Finally concat to a new Data Frame
    '''
    feature_series = pd.Series(feature)
    return pd.concat([df, feature_series], axis=1)

    
    
    

