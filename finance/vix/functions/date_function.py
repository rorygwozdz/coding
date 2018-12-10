#for finding the correlation between to dates on vix and spikes
def r_for_dates(start_date, end_date):
    dates_data = just_last_px.query('@start_date <= Date <= @end_date')
    corr_data = dates_data['vix_px_last'].corr(dates_data['spikes_px_last'])
    return corr_data

print r_for_dates(07/01/2018, 07/11/2018)
