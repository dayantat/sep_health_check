import pandas as pd
import json
from st2common.runners.base_action import Action

class Offline_in_SEPM(Action):

    def run(self,dataframe):
        try:
            df = pd.DataFrame.from_dict(dataframe)
            df = df.loc[~df["OPERATION_SYSTEM"].str.contains("Server")]
            return True, df
        except Exception as e:
            return False, {'error':e}
