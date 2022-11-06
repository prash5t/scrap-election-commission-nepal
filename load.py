# simple function to load/save voter's information after transforming, extracting

import pandas as pd
import os


# saves the ready data frame as csv to voters-warehouse directory
def save_csv(table_name, headers, rows):
    path = os.getcwd() + "/voters-warehouse"
    pd.DataFrame(rows, columns=headers).to_csv(
        os.path.join(path, f"{table_name}.csv"))
