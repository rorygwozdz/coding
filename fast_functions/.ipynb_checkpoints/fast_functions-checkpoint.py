import pandas as pd


def lookupD(s, format='%Y%m%d%H%M'):
    """Hella fast look up."""
    dates = {date: pd.to_datetime(date, format=format) for date in s.unique()}
    return s.map(dates)
