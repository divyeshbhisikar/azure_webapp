import snowflake.connector
import pandas as pd
import numpy as np
ctx = snowflake.connector.connect(
    account = 'pd91876.ap-south-1',
    user = 'Demo',
    schema = 'Public',
    warehouse='Compute_wh',
    role = 'accountadmin',
    password = 'Qwerty@1234'
)
cur = ctx.cursor()
query = '''select * from "test"."public"."B"'''
data = pd.read_sql(query, ctx)
print(data)
