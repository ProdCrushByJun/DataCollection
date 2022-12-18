#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine

sheet_id = '17Jbq7sGUNYT-jYhQjjBoW2ej78qsnbhIhMEC3RT0baI'
sheet_name = 'test1'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)
df.insert(0, 'TimeStamp', pd.to_datetime('now').replace(microsecond=0))

user = 'admin'
password = 'admin'
server = '83.220.170.164'
database = 'Reporting_AlfaCatalyst'

import sqlalchemy
SQLALCHEMY_DATABASE_URI = f'postgres+psycopg2://{user}:{password}@{server}/{database}'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
df.to_sql('CurrentIndicators', engine,if_exists = 'append',index = False)

