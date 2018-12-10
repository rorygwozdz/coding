#my derklicious import checker
print "Oh!"
import numpy as np
import pandas as pd
print "Derka, derka."

vix = pd.read_csv('/Users/rory/coding/vix/data/vix_data.csv')
spikes = pd.read_csv('/Users/rory/coding/vix/data/spikes_data.csv')


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

#turning dates to dates data
vix['Date'] = pd.to_datetime(vix['Date'])
spikes['Date'] = pd.to_datetime(spikes['Date'])
print vix['Date'][0] == spikes['Date'][0]




#just taking the last_px because the data here is longer (i.e. bloomberg doesn't have intraday for spikes past like 2016. Thanks, Bloomberg)
spikes_just_last_px = spikes.loc[:, ["Date", "spikes_px_last", "spikes_last_change", "spikes_last_pctchange"]]
vix_just_last_px = vix.loc[:, ["Date", "vix_px_last", "vix_last_change", 'vix_last_pctchange']]

#merging and dropping na data (I think i picked mistmatched dates or something so this alleviates that)
jlpx = spikes_just_last_px.merge(vix_just_last_px, on='Date').dropna()

print list(jlpx)
jlpx['nom_change_diff'] = (jlpx['vix_px_last'] - jlpx['spikes_px_last'])
print pd.(jlpx['nom_change_diff'])
