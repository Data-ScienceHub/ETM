import pandas as pd
from snowflake.snowpark import Session

class SnowparkConnector:
    '''
    Python class for connecting to Snowflake Data Warehouse using the Snowpark API
    
    API documentation: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/index.html
    '''

    def __init__(self, ACCOUNT, USER, PASSWORD, ROLE, WAREHOUSE, DATABASE, SCHEMA):
        '''
        Purpose: creates a new Snowpark connection session

        INPUTS:
        ACCOUNT - str snowpark account
        USER - str snowpark username
        PASSWORD - str snowpark user password
        ROLE - str snowpark role
        WAREHOUSE - str snowflake warehouse to access
        DATABASE - str snowflake database to access
        SCHEMA - str snowflake schema to access
        '''
        connection_parameters = {
            'account': ACCOUNT,
            'user': USER,
            'password': PASSWORD,
            'role': ROLE,
            'warehouse': WAREHOUSE,
            'database': DATABASE,
            'schema': SCHEMA
        }

        self.session = Session.builder.configs(connection_parameters).create()
    
    def query_snowpark(self, query):
        '''
        Purpose: Runs a query on snowpark and returns a Pandas dataframe with the results

        INPUTS:
        query - Snowflake query to run

        OUTPUTS:
        query_df - Pandas dataframe with the query results
        '''
        
        query_df = pd.DataFrame()
        try:
            print('Querying from Snowpark...')
            query_results = self.session.sql(query).collect()
            print('Snowpark query done')
            
            query_json = list(map(lambda x: x.as_dict(), query_results))
            query_df = pd.DataFrame(query_json)
        except Exception as e:
            print('Error querying from Snowpark:', e)
        
        return query_df
    
    def close_session(self):
        '''
        Purpose: Closes a snowpark session after running all queries needed.
        '''
        self.session.close_session()