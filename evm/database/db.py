import pandas as pd
from datetime import datetime as dt

NAS_URL = '/mnt/nfs_client/microk8s_datastore/events.xlsx'

def get_data():
    df = pd.read_excel(NAS_URL)
    df = df[df['Active'] == True]
    return df


def get_active(row):
    current = dt.date(dt.now())
    event = dt.date(dt(year=row['Year'], month=row['Month'], day=row['Day']))
    if current < event:
        action = 'Action'
    else:
        action = 'Drop'
    return action 

def countdown(row):
    current = dt.date(dt.now())
    event = dt.date(dt(year=row['Year'], month=row['Month'], day=row['Day'])) 
    days = (event - current).days
    w = divmod(days, 7)[0]
    d = divmod(days, 7)[1]
    return [w, d]

