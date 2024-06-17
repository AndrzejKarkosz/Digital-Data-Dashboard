
#-----------------------------------------DATA EXTRACT-------------------------------------------------
#impoort neccesary libraries
import pandas as pd
import numpy as np
import psycopg2 as ps
from sqlalchemy import create_engine
from sqlalchemy import Text

#extract raw data from datasource
csv_data = pd.read_excel(r"C:\Users\andrz\Desktop\Python\digital_data.xlsx")
df_raw = pd.DataFrame(data = csv_data)
df=df_raw

#-----------------------------------------DATA LOAD-------------------------------------------------
#establish connection with a database to load data
engine = create_engine('postgresql+psycopg2://postgres:12345@localhost/Digital data')
conn = engine.connect()

#load to sql
df.to_sql('brand_performance',conn, if_exists='replace')