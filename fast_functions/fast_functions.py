import pandas as pd


def lookupd(s, dateformat='%Y%m%d%H%M'):
    """Hella fast look up."""
    dates = {date: pd.to_datetime(date, format=dateformat) for date in s.unique()}
    return s.map(dates)
