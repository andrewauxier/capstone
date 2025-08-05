import pandas as pd


def eda(df: pd.DataFrame):
    """
    Run basic EDA on a dataframe.

    Args:
        Takes the desired dataframe as an argument.
    
    Returns:
        The column names, shape, data types, statistical description, and null values of the dataframe.
    """
    print('Columns:', df.columns)
    print('Shape:', df.shape)
    print('Data Types:', df.dtypes)
    print('Describe:', df.describe())
    print('Null Values:', df.isnull().sum())

### Function for handling null values in a dataframe ###
def remove_null(df:pd.DataFrame):

    """
    Removes the null values from a specified dataframe
    
    Args:
        Takes the desired dataframe as a argument
    
    Returns:
        Drops the null values and prints a summation of the null values in a dataframe (which should be 0).
    """
    df.dropna(inplace=True)
    print('Nulls are gone!', 
          df.isnull().sum())


