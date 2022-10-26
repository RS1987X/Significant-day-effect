# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:45:23 2021

@author: Richard
"""


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math
from datetime import date

#get prices from yahoo finance

tday = date.today()
tday_str = tday.strftime("%Y-%m-%d")

re_names = '8TRA.ST '\
'AAK.ST '\
'ABB.ST '\
'ALFA.ST '\
'ASSA-B.ST '\
'ATCO-A.ST '\
'AXFO.ST '\
'AZN.ST '\
'BALD-B.ST '\
'BETS-B.ST '\
'BILL.ST '\
'BOL.ST '\
'CAST.ST '\
'DOM.ST '\
'EKTA-B.ST '\
'ELUX-B.ST '\
'EMBRAC-B.ST '\
'EPI-A.ST '\
'EQT.ST '\
'ERIC-B.ST '\
'ESSITY-B.ST '\
'EVO.ST '\
'FABG.ST '\
'FING-B.ST '\
'GETI-B.ST '\
'HEXA-B.ST '\
'HM-B.ST '\
'HOLM-B.ST '\
'HPOL-B.ST '\
'HUSQ-B.ST '\
'ICA.ST '\
'INTRUM.ST '\
'JM.ST '\
'KIND-SDB.ST '\
'KINV-B.ST '\
'LUMI.ST '\
'LUNE.ST '\
'MTG-B.ST '\
'NCC-B.ST '\
'NDA-SE.ST '\
'NIBE-B.ST '\
'NOKIA-SEK.ST '\
'PCELL.ST '\
'SAAB-B.ST '\
'SAND.ST '\
'SAS.ST '\
'SCA-B.ST '\
'SEB-A.ST '\
'SECU-B.ST '\
'SHB-A.ST '\
'SKA-B.ST '\
'SKF-B.ST '\
'SOBI.ST '\
'SSAB-A.ST '\
'STE-R.ST '\
'SWED-A.ST '\
'SWMA.ST '\
'TEL2-B.ST '\
'TELIA.ST '\
'TIETOS.ST '\
'TIGO-SDB.ST '\
'TREL-B.ST '\
'VOLV-B.ST'\

#=============================================================================
# ============================================================================
hist = yf.download(re_names, start='2015-01-01', end=tday_str)
# ============================================================================
#=============================================================================


close_prices = hist["Adj Close"]#.dropna(how='all').fillna(0)
volumes = hist["Volume"].dropna(how='all').fillna(0)

r_vol=volumes/volumes.rolling(20).mean().shift(1)


#add current price
#close_prices = close_prices.drop('2020-01-01')
# =============================================================================
# =============================================================================
# index = close_prices.index.append(pd.Index([tday]))
# 
# close_prices = close_prices.append(pd.Series(), ignore_index=True)
# close_prices=close_prices.set_index(index)
# 
# re_names_df = re_names.split(" ")
# for x in re_names_df:
#      stock_data = yf.Ticker(x)
#      curr_mid = (stock_data.info["bid"] + stock_data.info["ask"])/2
#      close_prices.loc[close_prices.tail(1).index,x] = curr_mid
# =============================================================================

# =============================================================================

#calculate daily returns
ret_daily = close_prices.pct_change()


#create binary dataframe to exclude stocks with big move large volume days in the last n sessions
significant_days = (r_vol > 2.75) & (ret_daily > 0) & (ret_daily < 0.08)
 
#create position indicator df
long_ind = significant_days.shift(1)

#long_ind = (ret_5d < 0) 
#replace false with NaN to avoid 0s impacting the mean
long_ind = long_ind.replace(False, np.nan)
long_returns_daily = ret_daily*long_ind


#calc transaction cost
trans = long_ind
n_trans = trans.count().sum()

trans_value = n_trans*100000
total_trans_cost = n_trans*29

trans_proc_fee = total_trans_cost/trans_value

#daily returns of long short strategy
#avg_long_ret = starting_capital*long_returns_daily.mean(axis=1)-transaction_cost
avg_long_ret = long_returns_daily.mean(axis=1)-trans_proc_fee
#avg_short_ret = short_returns_daily.mean(axis=1)-trans_proc_fee
daily_returns_strat = avg_long_ret.dropna(how='all').fillna(0) #+avg_short_ret

#avg_daily_rets  = daily_returns_strat.mean(axis=1)

#Cumulative returns 
#cum_ret =starting_capital +  np.cumsum(daily_returns_strat) #
cum_ret =(1 + daily_returns_strat).cumprod()
#cum_long_ret =  (1 + avg_long_ret).cumprod()
#cum_short_ret =  (1 + avg_short_ret).cumprod()


###########################################
#stats for basic strategy
##########################################

print("Basic strategy:   ")
print('Significant day effect LARGE CAP')
mean_ret = cum_ret.tail(1)**(1/7)-1
print("CAGR " + str(mean_ret[0]))
vol = (daily_returns_strat.std()*math.sqrt(82))
sharpe = mean_ret/vol
kelly_f = mean_ret/vol**2
print("Volatility " + str(vol))
print("Sharpe " + str(sharpe[0]))
print("Kelly fraction " + str(kelly_f[0]))
#maxiumum drawdown
Roll_Max = cum_ret.cummax()
Daily_Drawdown = cum_ret/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.cummin()
print("Max drawdown " + str(Max_Daily_Drawdown.tail(1)[0]))

#plots
plt.plot(cum_ret)
#plt.plot(cum_long_ret)
#plt.plot(cum_short_ret)
#plt.plot(Daily_Drawdown)


###################################################
#modified strategy considering factor momentum
####################################################
mom_cum_ret = (1+daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0]).cumprod()
#mom_cum_ret = starting_capital + np.cumsum(daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0])
mom_daily_ret_RE = mom_cum_ret.pct_change()


mom_mean_ret = mom_cum_ret.tail(1)**(1/7)-1

mom_vol = (daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0].std()*math.sqrt(82))
mom_sharpe = mom_mean_ret/mom_vol
mom_kelly_f = mom_mean_ret/mom_vol**2

#maxiumum drawdown
mom_Roll_Max = mom_cum_ret.cummax()
mom_Daily_Drawdown = mom_cum_ret/mom_Roll_Max - 1.0
mom_Max_Daily_Drawdown = mom_Daily_Drawdown.cummin()
print("Factor momentum:   ")
print('Significant day effect with momentum LARGE CAP')
print("CAGR " + str(mom_mean_ret[0]))
print("Volatility " + str(mom_vol))

print("Sharpe " + str(mom_sharpe[0]))
print("Kelly fraction " + str(mom_kelly_f[0]))
#maxiumum drawdown
Roll_Max = cum_ret.cummax()
Daily_Drawdown = cum_ret/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.cummin()
print("Max drawdown " + str(mom_Max_Daily_Drawdown.tail(1)[0]))

#calculate log returns st reversal momentum strategy and print returns per year
mom_log_ret_RE = np.log(mom_cum_ret)-np.log(mom_cum_ret.shift(1))
per = mom_log_ret_RE.index.to_period("Y")
g = mom_log_ret_RE.groupby(per)
ret_per_year = g.sum()
print("   ")
print("signigficant day effect with factor momentum returns per year")
print(ret_per_year)


per_M = mom_log_ret_RE.index.to_period("M")
grouping_month = mom_log_ret_RE.groupby(per_M)
ret_per_month = grouping_month.sum()
#stats for monthly returns
percent_positive = ret_per_month[ret_per_month>0].count()/ret_per_month.count()
print("")
print("percent positive months " + str(percent_positive))


plt.plot(mom_cum_ret)

################
#buy and hold
#################

avg_ret_boh= ret_daily.mean(axis=1)
cum_ret_boh =  (1 + avg_ret_boh).cumprod()
#avg_ret_boh= starting_capital*ret_daily.mean(axis=1)
#cum_ret_boh =  starting_capital + np.cumsum(avg_ret_boh)
plt.plot(cum_ret_boh)

#stats buy and hold
print(" Buy and Hold  ")
print('Buy and hold stats')
boh_mean_ret = cum_ret_boh.tail(1)**(1/7)-1
boh_vol = (avg_ret_boh.std()*math.sqrt(252))
boh_sharpe = boh_mean_ret/boh_vol
boh_kelly_f = boh_mean_ret/boh_vol**2

#maxiumum drawdown
boh_Roll_Max = cum_ret_boh.cummax()
boh_Daily_Drawdown = cum_ret_boh/boh_Roll_Max - 1.0
boh_Max_Daily_Drawdown = boh_Daily_Drawdown.cummin()



print("CAGR " + str(boh_mean_ret[0]))
print("Volatility " + str(boh_vol))

print("Sharpe " + str(boh_sharpe[0]))
print("Kelly fraction " + str(boh_kelly_f[0]))

print("Max drawdown " + str(boh_Max_Daily_Drawdown.tail(1)[0]))





print("   ")
print('20-day momentum of significant day effect strategy')
print(cum_ret.pct_change(20).tail(1))

