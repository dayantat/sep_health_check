import pandas as pd
import json
import pymssql
from st2common.runners.base_action import Action

class Whats_my_name(Action):

    def run(self,db_user,db_server,db_password,db_name,sql_query):
        try:
            print("Checking the Parameters:", db_user,db_server,db_password,db_name,sql_query)
            conn = pymssql.connect(db_server, db_user, db_password,db_name)

            if conn:
                df = pd.read_sql(sql_query,conn)
                df = df.to_json()
                df = json.loads(df)
                return True, df
            else:
                return False, {"name": "Failed"}
        except Exception as e:
            return False, {'error':e}