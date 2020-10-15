import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def count_uniques(df):
    n_unique = {}
    pct_unique = {}
    rows = len(df)
    for i in range(df.shape[1]):
        col = df.columns[i]
        n_unique[col] = df[col].nunique()
        pct_unique[col] = n_unique[col] / rows
    f = pd.DataFrame([n_unique, pct_unique], index = ['n_unique','pct_unique']).transpose()
    f['n_unique'] = f['n_unique'].astype(int)
    return f

# df['date'] = pd.DatetimeIndex(df['SQAnalysisDate']).strftime('%Y-%m')

def analyze_(df):
    print(f'Number of rows: {df.shape[0]}')
    print(f'Number of columns: {df.shape[1]}')
    print(f'Uniques stats:')
    print(count_uniques(df))
    
    for col in df.columns:
        print(f'\nColumn {col}:')
        if col == 'refactoringType' or col == 'projectID':
            print(f'\t TYPES: {set(df[col])}')
        elif col == 'faultFixingTimestamp' or col == 'faultInducingTimestamp': 
            print(pd.DatetimeIndex(df[col]).strftime('%Y-%m-%d'))
        else: 
            print(f'\t{[i for i in df[col][0:15]]}')

conn = sqlite3.connect('data/technicalDebtDataset.db')

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = set([table[0] for table in cursor.fetchall()])

table = 'SONAR_RULES'

if table in table_names:
    df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
    print(df.columns)

    #analyze_(df)

    #fig, ax = plt.subplots(1,1,figsize=(15,15))
    #sns.heatmap(pd.crosstab(df.projectID, df.refactoringType), ax=ax)
    #plt.show()

    """
    fault_ind = pd.DatetimeIndex(df['faultInducingTimestamp']).strftime('%Y-%m-%d').to_series()
    fault_fix = pd.DatetimeIndex(df['faultFixingTimestamp']).strftime('%Y-%m-%d').to_series()
    fault_ind.reset_index(drop = True, inplace = True)
    fault_fix.reset_index(drop = True, inplace = True)

    dff = pd.concat((fault_ind, fault_fix), axis=1)
    dff['time_induced'] = pd.to_datetime(dff['faultInducingTimestamp'])
    dff['time_fixed'] = pd.to_datetime(dff['faultFixingTimestamp'])
    df['time2fix']  = dff['time_fixed'] - dff['time_induced']
    df = df[['projectID','time2fix']]
    
    print(df.groupby(['projectID']).mean(numeric_only=False))
    grouped_df = df.groupby(['projectID']).mean(numeric_only=False)
    print(grouped_df['time2fix'].apply(lambda x: (x / np.timedelta64(1, 'D')/7)))

    plt.bar(range(grouped_df.shape[0]), grouped_df['time2fix'].apply(lambda x: (x / np.timedelta64(1, 'D')/7)))
    plt.xlabel('Project')
    plt.xticks(range(grouped_df.shape[0]), grouped_df.index)
    plt.xticks(rotation=90)
    plt.ylabel('Average number of weeks to fix')
    plt.show()
    """
    analyze_(df)

    print(set(df['description_format']))



