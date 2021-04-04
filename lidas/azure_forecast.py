import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm

def forecast(region):
    df = pd.read_csv('./data/Cases_ByState.csv')
    
    df_region = df[df['region']==region].reset_index(drop=True)[['date','cases']]
    df_region['date']= pd.to_datetime(df['date'],format='%d-%b-%y')
    y = df_region.set_index(['date']).sort_values(by="date",ascending=True)
    mod = sm.tsa.SARIMAX(y, order=(1, 1, 1), trend='c')
    res = mod.fit()
    
    pred = res.get_forecast(steps=28)
    t= pred.summary_frame()
    
    fig, ax = plt.subplots(figsize=(15, 10))
    df_region['cases'].loc['2020-10-01':].plot(ax=ax)
    
    t['mean'].plot(ax=ax, style='k--')
    ax.fill_between(t.index, t['mean_ci_lower'], t['mean_ci_upper'], color='k', alpha=0.1)
    ax.set_xlabel('Date')
    ax.set_ylabel('NO. of Cases')
    fig
    
    return fig