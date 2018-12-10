
def r_for_vix_pctmove(type, low_pct, high_pct):
        if type == 'between':
            between = just_last_px.query('@low_pct <= vix_last_pctchange <= @high_pct')
            corr_between = between['']

        if type == 'outside':
            outside = just_last_px.query('@low_pct >= vix_last_pctchange <= @high_pct')

        if type == 'above':
            above = just_last_px.query('@low_pct >= vix_last_pctchange <= @high_pct')

        if type == 'below':
            below = just_last_px.query('@low_pct >= vix_last_pctchange <= @high_pct')
