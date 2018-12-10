#my derklicious import checker
print "Oh!"
import numpy as np
import pandas as pd
print "Derka, derka."

#loading the vix/spikes csv's from bloomberg ("no secuirty = this" garbage at the top, just the price data).
#I'll probably need to make a program that can do this for any security, ever, at all. MAybe I'll learn to query bloomberg haha.
vix = pd.read_csv('/Users/rory/coding/vix/data/vix_data.csv', infer_datetime_format = True)
spikes = pd.read_csv('/Users/rory/coding/vix/data/spikes_data.csv', infer_datetime_format = True)


#renaming them for unique merging later
spikes = spikes.rename(index = str, columns = {
    #last format
    "PX_LAST": "spikes_px_last",
        "Change": "spikes_last_change",
        '% Change': "spikes_last_pctchange",
    #open format
    "PX_OPEN": "spikes_px_open",
        "Change.1": "spikes_open_change",
        '% Change.1': "spikes_open_pctchange",
    #high format
    "PX_HIGH": "spikes_px_high",
        "Change.2": "spikes_high_change",
        '% Change.2': "spikes_high_pctchange",
    #low format
    "PX_LOW": "spikes_px_low",
        "Change.3": "spikes_low_change",
        '% Change.3': "spikes_low_pctchange"})
vix = vix.rename(index = str, columns = {
    #last format
    "PX_LAST": "vix_px_last",
        "Change": "vix_last_change",
        '% Change': "vix_last_pctchange",
    #open format
    "PX_OPEN": "vix_px_open",
        "Change.1": "vix_open_change",
        '% Change.1': "vix_open_pctchange",
    #high format
    "PX_HIGH": "vix_px_high",
        "Change.2": "vix_high_change",
        '% Change.2': "vix_high_pctchange",
    #low format
    "PX_LOW": "vix_px_low",
        "Change.3": "vix_low_change",
        '% Change.3': "vix_low_pctchange"})

#just taking the last_px because the data here is longer (i.e. bloomberg doesn't have intraday for spikes past like 2016. Thanks, Bloomberg)
spikes_just_last_px = spikes.loc[:, ["Date", "spikes_px_last", "spikes_last_change", "spikes_last_pctchange"]]
vix_just_last_px = vix.loc[:, ["Date", "vix_px_last", "vix_last_change", 'vix_last_pctchange']]

#merging and dropping na data (I think i picked mistmatched dates or something so this alleviates that)
just_last_px = spikes_just_last_px.merge(vix_just_last_px, on='Date')
just_last_px = just_last_px.dropna()
just_last_px['Date'] = pd.to_datetime(just_last_px['Date'])

def get_corr(df):
    corr = df['vix_px_last'].corr(df['spikes_px_last'])
    return corr

#for returning the correlation of vix and spikes for different pct moves. Inputs for type are 'between', 'outside', 'above', and 'below'
#the pcts are low_pct and high_pct for between and outside and for above/below so you can just enter low_pct
def r_for_vix_pctmove(type, low_pct, high_pct=0):
        if type == 'between':
            df = just_last_px.query('@low_pct <= vix_last_pctchange <= @high_pct')
        elif type == 'outside':
            df = just_last_px.query('@low_pct >= vix_last_pctchange or vix_last_pctchange >= @high_pct')
        elif type == 'above':
            df = just_last_px.query('vix_last_pctchange >= @low_pct')
        elif type == 'below':
            df = just_last_px.query('vix_last_pctchange <= @low_pct ')
        else:
            return "Check your spelling ~ you wrote '%s' but the options are %s" % (type, 'between, outside, above, and below.')
        return get_corr(df)


def avg_and_med(df):
    df_vix = df['vix_px_last'].values
    df_spikes = df['spikes_px_last'].values
    mag = df_vix - df_spikes
    avg_diff = np.mean(mag).round(3)
    med_diff = np.median(mag).round(3)
    return avg_diff, med_diff

#returns avgerage difference and median difference in an array or tuple idk which
def magnitude_difference(type, low_num, high_num=0):
    if type == 'between':
        df = just_last_px.query("@low_num <= vix_px_last <= @high_num")
    elif type == 'above':
        df = just_last_px.query("@low_num <= vix_px_last")
    elif type == 'below':
        df = just_last_px.query("@low_num >= vix_px_last")
    elif type == 'outside':
        df = just_last_px.query("@low_num >= vix_px_last or vix_px_last >= @high_num")
    else:
        return "Check your spelling ~ you wrote '%s' but the options are %s" % (type, 'between, outside, above, and below.')
    return avg_and_med(df)


def print_mean(type, low_num, high_num=0):
    mean = magnitude_difference(type, low_num, high_num)[0]
    if high_num != 0:
        print("The mean magnitude difference %s %s and %s is %s." %\
            (type, low_num, high_num, mean))
    else:
        print("The mean magnitude difference %s %s is %s." %\
            (type, low_num, mean))

def print_median(type, low_num, high_num=0):
    median = magnitude_difference(type, low_num, high_num)[1]
    if high_num != 0:
        print("The median magnitude difference %s %s and %s is %s." %\
            (type, low_num, high_num, median))
    else:
        print("The median magnitude difference %s %s is %s." %\
            (type, low_num, median))

def print_mm(type, low_num, high_num=0, is_mean=False, is_median=False):
    if not is_mean and not is_median:
        print("insert error")
        return None
    if is_mean:
        print_mean(type, low_num, high_num)
    if is_median:
        print_median(type, low_num, high_num)

def date_corr_btwn(far_date, close_date):
    der = pd.to_datetime(far_date)
    ka = pd.to_datetime(close_date)
    older_than = just_last_px.loc[just_last_px['Date'] >= der, :]
    but_younger_than = older_than.loc[older_than.Date <= ka, :]
    corr_btwn = but_younger_than['vix_px_last'].corr(but_younger_than['spikes_px_last'])
    return corr_btwn


def get_date_corr_btwn(first_date, last_date):
    corr_btwn = date_corr_btwn(first_date, last_date)
    corr_btwn = np.round(corr_btwn, 3)
    string = "The correlation between %s and %s is %s." %\
     (first_date, last_date, corr_btwn)
    return string
