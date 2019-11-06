"""
19AU CSE583 HW4 Python Programming Style
Testing the functionality of the functions in HW3
"""

import pandas as pd

def read_csv_from_url(url):
    """
    Read CSV From URL
    Input: a url of a csv file
    Return: pandas dataframe
    """
    data_frame = pd.read_csv(url)
    return data_frame


def test_create_dataframe(data_frame, list_of_col):
    """
    Testing whether a dataframe satisfy the following conditions:
    The DataFrame contains only the columns that you specified as the second argument.
    The values in each column have the same python type
    There are at least 10 rows in the DataFrame.
    Input: pandas dataframe, a list of column names
    Output: True or False
    """
    temp = list(data_frame)
    for i in temp:
        if i not in list_of_col:
            return False
    if len(data_frame) < 10:
        return False
    for i in range(len(temp)):
        prev_type = type(data_frame[temp[i]][0])
        for j in range(1, len(data_frame)):
            if type(data_frame[temp[i]][j]) != prev_type:
                return False
            prev_type = type(data_frame[temp[i]][j])
    return True

def test_correct_type(data_frame):
    """
     testing whether all columns have values of the correct type
     Input: pandas dataframe
     Output: True or False
    """
    temp = list(data_frame)
    for i in range(len(temp)):
        prev_type = type(data_frame[temp[i]][0])
        for j in range(1, len(data_frame)):
            if type(data_frame[temp[i]][j]) != prev_type:
                return False
            prev_type = type(data_frame[temp[i]][j])
    return True


def check_nan_values(data_frame):
    """
     checking nan values or not
     Input: pandas dataframe
     Output: True or False
    """
    if data_frame.isna().sum().any() > 0:
        print("Nan values !")
    else:
        print("No Nan values.")


def least_one_row(data_frame):
    """
    checking at least one row in dataframe
    Input: pandas dataframe
    Output: True or False
    """
    if data_frame:
        return True
    return False

CSV = read_csv_from_url("https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD")

test_correct_type(CSV)

check_nan_values(CSV)

least_one_row(CSV)
