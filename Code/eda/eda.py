import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from snowflake.snowpark import Session

load_dotenv()

ACCOUNT = os.getenv('ACCOUNT')
USER = os.getenv('SP_USER')
PASSWORD = os.getenv('PASSWORD')
ROLE = os.getenv('ROLE')
WAREHOUSE = os.getenv('WAREHOUSE')
DATABASE = os.getenv('DATABASE')
SCHEMA = os.getenv('SCHEMA')

connection_parameters = {
    'account': ACCOUNT,
    'user': USER,
    'password': PASSWORD,
    'role': ROLE,
    'warehouse': WAREHOUSE,
    'database': DATABASE,
    'schema': SCHEMA
}

test_session = Session.builder.configs(connection_parameters).create()

print('session built')

events_query = """
SELECT 
    DATE_TRUNC('month', day) AS month
    , event
    , COUNT(id) AS ids
    , COUNT(DISTINCT set_profile) AS profiles
    , COUNT(DISTINCT set_user) AS users
FROM event
WHERE DATE_TRUNC('year', day) = DATE('2022-01-01')
GROUP BY 1, 2
ORDER BY 1, 3 DESC
"""

print('querying...')
query_results = test_session.sql(events_query).collect()
print('query done')
test_session.close()
print('session closed')


# convert to pandas df
query_json = list(map(lambda x: x.as_dict(), query_results))
query_df = pd.DataFrame(query_json)
query_df.to_csv('events_data.csv', index = 0)
# query_df = pd.read_csv('events_data.csv')

# create simple plot
query_df.set_index('MONTH', inplace=True)
query_df.groupby('EVENT')['IDS'].plot(legend = True)
plt.savefig('events.png')