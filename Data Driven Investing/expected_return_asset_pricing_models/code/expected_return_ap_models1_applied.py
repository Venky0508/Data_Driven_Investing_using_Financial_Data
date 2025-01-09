import pandas as pd


def getExpectedReturn(df, price_col_name, annualised=True, annualise_method='sophisticated'):
    """
    Returns the expected return of a security given price data.
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


sp500 = pd.read_csv("../data/sp500_price.csv")

# Annualised Expected Return of the Market (E[r_m]) - sophisticated method
# remember that the default value for 'annualised' is True
getExpectedReturn(df=sp500, price_col_name='sp500')

# Annualised Expected Return of the Market (E[r_m]) - crude method
getExpectedReturn(df=sp500, price_col_name='sp500', annualise_method='crude')


def CAPM_expected_return(r_f, expected_return_market, beta_j):
    """
    Returns the Expected Return of a security using the CAPM formula.
    Can use the function getExpectedReturn() to set the expected_return_market parameter.
    """
    expected_return_capm = r_f + beta_j * (expected_return_market - r_f)

    return expected_return_capm


# Use the getExpectedReturn() function inside the CAPM_expected_return() function
CAPM_expected_return(
    r_f=0.0309,  # being the 10 year yield on US Treasuries, obtained from the FT at the time of recording.
    expected_return_market=getExpectedReturn(df=sp500, price_col_name='sp500'),
    beta_j=1.1233)  # being the Beta of Alphabet Inc (GOOGL) obtained from the FT at the time of recording.

# Note that this gives us the same E[r_GOOGL] = 15.18% estimated manually in the lecture.
