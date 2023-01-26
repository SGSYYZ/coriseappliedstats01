import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function to find the most profitable product for a given year and quarter
def most_profitable_product(data: pd.DataFrame, year: int, quarter: int) -> str:
    """
    Find the most profitable product for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to find the most profitable product for
    :param quarter: The quarter to find the most profitable product for
    :return: The most profitable product for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)
    data['ProductTotalPriceSum'] = data.groupby('Description')['TotalPrice'].transform('sum')
    # Find the most profitable product
    return return data[data.ProductTotalPriceSum == data.ProductTotalPriceSum.max()]['Description'].values[0]
