import numpy as np 
import pandas as pd 

df=pd.read_csv("Cases_ByState_Updated.csv")

#there is comma "," character and need to remove this in order to convert to numeric for computation
df.replace(to_replace=[r','],
           value=[''],
           regex=True, 
           inplace=True)

#copy dataframe to new dataframe for numbers in bracket
df_inc = df.copy()

#extract numbers in bracket for new dataframe
cols=[i for i in df_inc.columns if i not in ["Date"]]

for col in cols:
    df_inc[col]=df_inc[col].str.extract(r"\((.*?)\)", expand=False)
    
#replace Nan to 0 for df
df = df.replace(np.nan,0)
#replace NaN to 0 for df_inc
df_inc = df_inc.replace(np.nan,0)

#remove numbers in bracket
df.replace(to_replace=[r'\(([^)]+)\)'],
           value=[''],
           regex=True, 
           inplace=True)
#change all dtype to int64 except date
cols=[i for i in df.columns if i not in ["Date"]]
for col in cols:
    df[col]=pd.to_numeric(df[col])

df.Date=df.Date+'/2020'
df = df.melt(id_vars = 'Date', var_name = 'State', value_name = 'Cases')
state_name = {'JH':'Johor', 'KD':'Kedah', 'KE':'Kelantan', 'ML':'Malacca', 'NS':'Negeri Sembilan', 'PH':'Pahang', 'PG':'Penang', 'PK':'Perak', 'PR':'Perlis', 'SB':'Sabah', 'SR':'Sarawak', 'SE':'Selangor', 'TR':'Terengganu', 
                                  'KL':'Kuala Lumpur', 'PT':'Putrajaya', 'LB':'Labuan'}
df['State'] = [state_name[i] for i in df['State']]
df.to_csv('Cases_ByState_Cleaned.csv',index = False)