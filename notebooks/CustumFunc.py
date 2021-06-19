import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

def isitnull(x):    
    if pd.isnull(x):
        return 0
    else: 
        return 1

# Created a function to display distribution
def prospect(df,i,j):
    count_prospects = df.groupby(i)[j].sum().reset_index(name = 'total_defaults')
    No_of_prospect_job = df.groupby(i)[j].count().reset_index(name = 'Total_Records')
    agg = count_prospects.merge(No_of_prospect_job, on = i)
    agg['default_rate'] = 100*(agg['total_defaults']/agg['Total_Records']).round(4)
    print(agg)
    ax = sns.barplot(x=i, y='default_rate', data=agg)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    plt.show()


