import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function using the Poisson distribution to model how likely a customer is to arrive on the website in the next 15 minutes
def customer_arrival_proba(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the probability of a customer arriving on the website in the next 15 minutes
    :param data: The dataframe containing the data
    :param year: The year to calculate the probability for
    :param quarter: The quarter to calculate the probability for
    :return: The probability of a customer arriving on the website in the next 15 minutes
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Calulate the mean number of customers per day
    mu = (data
            .groupby(data.Month.astype(str)+"-"+data.Day.astype(str))
            ['CustomerID'].nunique()
            .mean()
            )
    
    # Generate the Poisson distribution
    distribution = poisson.cdf(1.1*mu, mu)

    # Calculate the probability of having 10% more customers on a given day
    return round(1 - mycdf,4)
