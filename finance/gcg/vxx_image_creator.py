import numpy as np
import pandas as pd
import scipy.stats as sc
import matplotlib.pyplot as plt


vxx = pd.read_excel('data/worksheet_of_em_all.xlsx', sheet_name ='VXX')
dates = pd.to_datetime(vxx.date)
vxx["date"] = dates
plt.plot_date(vxx.date, vxx.close,  ls = 'solid', ms = .2, color = 'blue')
plt.title("VXX")
plt.xlabel("Date")
plt.ylabel("Price in Dollars")
i = 'VXX'
pchartimgfilename = ('images/' + i + '/pricechart.png')
plt.savefig(pchartimgfilename)
plt.close()
vxx['returns'] = vxx.open/vxx.close - 1
plt.plot_date(vxx.date, vxx.returns, ls = 'solid', ms = .15, color = 'gold')
plt.title("VXX Returns in Decimal")
plt.ylabel("Returns in Decimal")
plt.xlabel("Date")
derkfilename = ('images/' + i + '/derk.png')
plt.savefig(derkfilename)
plt.close()
vxx_sorted_returns = vxx['returns'].sort_values().reset_index(drop = True)
vxx_cdf = (np.arange(len(vxx_sorted_returns)) +1)/len(vxx_sorted_returns)
(np.arange(len(vxx_sorted_returns)) +1)
vxx_true_cdf = []
for i in np.arange(len(vxx_cdf)):
    if vxx_sorted_returns[i] <= 0:
        vxx_true_cdf += [vxx_cdf[i]]
        if i == 0:
            vxx_true_cdf[i] = vxx_true_cdf[i]/2
    else:
        vxx_true_cdf += [1-vxx_cdf[i]]
        if vxx_true_cdf[i] == 0:
            #there is some non zero that the edge case, or final point is chosen
            #i.e. the value of it's true cdf != 1-1
            #so I'm setting it as equal probability to the farr left one (which was divided by two)
            vxx_true_cdf[i] = vxx_true_cdf[0]



vxx_distributed_returns = pd.DataFrame({'returns': vxx_sorted_returns,
                                       'true_cdf': vxx_true_cdf})
plt.plot(vxx_distributed_returns.returns, vxx_distributed_returns.true_cdf)
plt.yscale('log')
plt.title('VXX Logarized Returns')
plt.ylabel('Log CDF')
plt.xlabel('Returns')
plt.ylabel("Price in Dollars")
i = 'VXX'
derkafilename = ('images/' + i + '/derka.png')
plt.savefig(derkafilename)
abover = 3
vxx_norm = (vxx_distributed_returns.returns - np.mean(vxx_distributed_returns.returns))/np.std(vxx_distributed_returns.returns)
vxx_norm_above = abs(vxx_norm[abs(vxx_norm) > abover])
vxx_log_return = np.log(vxx_distributed_returns.true_cdf)
vxx_log_above =  vxx_log_return[abs(vxx_norm) > abover]
###vxx_norm_above == t_norm_x, vxx_log_above == dvariable (this all references earlier code)
plt.scatter(vxx_norm_above, vxx_log_above)
plt.title("VXX Log Log Big Returns")
plt.xlabel("Log Normalized Returns)")
plt.ylabel("Log CDF")
plt.plot(np.unique(vxx_norm_above), np.poly1d(np.polyfit(vxx_norm_above, vxx_log_above, 1))(np.unique(vxx_norm_above)), color = 'red')
i = 'VXX'
derkaafilename = ('images/' + i + '/derkaa.png')
plt.savefig(derkaafilename)
plt.close()
