#my derklicious import checker
print "Oh!"
import numpy as np
import pandas as pd
print "Derka, derka."

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

print get_date_corr_btwn("0/18", "07/10/18")
