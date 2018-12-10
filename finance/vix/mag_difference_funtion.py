be = 13
tween = 20

samp = just_last_px.query('@be <= vix_px_last <= @tween')
print samp['vix_px_last']



def magnitude_difference(type, high_num, low_num = 0):
    if type == 'between':
            df = just_last_px.query("@low_num <= vix_px_last <= @high_num")
            df_vix = df['vix_px_last']
            mag = df_vix.sub(df_spikes['spikes_px_last'], axis = 0)
            avg_diff = np.mean(mag)
            return avg_diff
    elif type == 'above':
            above = just_last_px.query("@high_num <= vix_px_last")df_spikes = df['spikes_px_last']
