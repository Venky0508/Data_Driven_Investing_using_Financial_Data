# © Copyright, Fervent | All Rights Reserved
"""
# =====================================================
#   EXPECTED RETURNS USING MEAN - CREATING A FUNCTION
# =====================================================

# -----------
#  Beginner?
# -----------
We STRONGLY recommend using the .ipynb version instead of this .py version
The .ipynb has more explanatory notes to help and guide you through.

The .py version is largely designed for more intermediate / advanced users of
Python.
"""

import pandas as pd

data = pd.read_csv("../data/fb_price.csv")


# Version 1: Calculates daily Expected Return
def getExpectedReturn(df, price_col_name):
    """
    Returns the expected return of a stock given price data.
    """

    # Calculate returns of prices
    returns = df[price_col_name].pct_change(1)  # Make sure you don't call this "return"!

    # Calculate the expected return using the mean method
    expected_return = returns.mean()

    return expected_return


getExpectedReturn(df=data, price_col_name='Adj Close')


# Version 2: Calculates Daily and Annualised Expected Returns,
# annualising by the 'crude' or 'sophisticated' method.
def getExpectedReturn(df, price_col_name, annualised=True, annualise_method='sophisticated'):
    """
    Returns the expected return of a stock given price data.
    """

    # Calculate returns of prices
    returns = df[price_col_name].pct_change(1)

    # Calculate the expected return using the mean method
    expected_return_daily = returns.mean()

    if annualised:
        if annualise_method == 'sophisticated':
            expected_return_annual = ((1 + expected_return_daily) ** 250) - 1
        elif annualise_method == 'crude':
            # Crude method
            expected_return_annual = expected_return_daily * 250

        return expected_return_annual

    else:
        return expected_return_daily


# Annualised Expected Return (sophisticated method)
getExpectedReturn(data, 'Adj Close')

# Daily expected return
getExpectedReturn(data, 'Adj Close', annualised=False)

# Annualised Expected Return (crude method)
getExpectedReturn(data, 'Adj Close', annualise_method='crude')
