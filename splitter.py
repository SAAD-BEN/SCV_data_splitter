import os
import sys
import argparse
import numpy as np
import pandas as pd


# split data from a csv file into a given percentage of json and sql files
def split_data(csv_file, json_file, sql_file, json_percent):
    # read csv file
    df = pd.read_csv(csv_file, header=None)
    # get number of rows
    num_rows = df.shape[0]
    # get number of json rows
    num_json_rows = int(num_rows * json_percent)
    # get number of sql rows
    num_sql_rows = num_rows - num_json_rows
    # get random indices for json rows
    json_indices = np.random.choice(num_rows, num_json_rows, replace=False)
    # get random indices for sql rows
    sql_indices = np.random.choice(num_rows, num_sql_rows, replace=False)
    # get json rows
    json_rows = df.iloc[json_indices]
    # get sql rows
    sql_rows = df.iloc[sql_indices]
    # write json rows to json file
    json_rows.to_json(json_file, orient='records', lines=True)
    # write sql rows to sql file
    sql_rows.to_csv(sql_file, index=False, header=False)