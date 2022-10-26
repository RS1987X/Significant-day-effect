# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:20:01 2022

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

tickers = "EVO.ST "\
"ORRON.ST "\
"INVE-B.ST "\
"HM-B.ST "\
"ERIC-B.ST "\
"NDA-SE.ST "\
"AZN.ST "\
"VOLV-B.ST "\
"GETI-B.ST "\
"SAND.ST "\
"SWMA.ST "\
"ATCO-A.ST "\
"SWED-A.ST "\
"BOL.ST "\
"ESSITY-B.ST "\
"SEB-A.ST "\
"EMBRAC-B.ST "\
"SINCH.ST "\
"ASSA-B.ST "\
"HEXA-B.ST "\
"ABB.ST "\
"NIBE-B.ST "\
"EQT.ST "\
"SKF-B.ST "\
"VOLCAR-B.ST "\
"ELUX-B.ST "\
"TELIA.ST "\
"SBB-B.ST "\
"SHB-A.ST "\
"LIFCO-B.ST "\
"SAGA-B.ST "\
"TEL2-B.ST "\
"ALFA.ST "\
"ATCO-B.ST "\
"CAST.ST "\
"ONCO.ST "\
"SSAB-B.ST "\
"SCA-B.ST "\
"ALIV-SDB.ST "\
"KINV-B.ST "\
"EPI-A.ST "\
"HUSQ-B.ST "\
"SKA-B.ST "\
"SF.ST "\
"BALD-B.ST "\
"SOBI.ST "\
"TIGO-SDB.ST "\
"NIVI-B.ST "\
"HTRO.ST "\
"TREL-B.ST "\
"SECU-B.ST "\
"INDU-C.ST "\
"EKTA-B.ST "\
"KIND-SDB.ST "\
"SSAB-A.ST "\
"LUND-B.ST "\
"AZA.ST "\
"LATO-B.ST "\
"SAVE.ST "\
"EPI-B.ST "\
"STOR-B.ST "\
"AXFO.ST "\
"PCELL.ST "\
"KLARA-B.ST "\
"SHOT.ST "\
"DOM.ST "\
"SECT-B.ST "\
"INDT.ST "\
"BICO.ST "\
"ADDT-B.ST "\
"BILL.ST "\
"CTEK.ST "\
"TRUE-B.ST "\
"THULE.ST "\
"FABG.ST "\
"HOLM-B.ST "\
"HUFV-A.ST "\
"ALIF-B.ST "\
"INTRUM.ST "\
"KAMBI.ST "\
"SAS.ST "\
"MIPS.ST "\
"FING-B.ST "\
"VESTUM.ST "\
"AAK.ST "\
"VITR.ST "\
"WIHL.ST "\
"HUMBLE.ST "\
"BHG.ST "\
"JM.ST "\
"AEGIR.ST "\
"INSTAL.ST "\
"BEIJ-B.ST "\
"SAAB-B.ST "\
"HPOL-B.ST "\
"CTM.ST "\
"STORY-B.ST "\
"BOOZT.ST "\
"CIBUS.ST "\
"LIAB.ST "\
"NYF.ST "\
"VNV.ST "\
"WALL-B.ST "\
"STE-R.ST "\
"CINT.ST "\
"BETS-B.ST "\
"SWEC-B.ST "\
"NETI-B.ST "\
"HEM.ST "\
"VIT-B.ST "\
"VIMIAN.ST "\
"BURE.ST "\
"RATO-B.ST "\
"DIOS.ST "\
"PNDX-B.ST "\
"LOOMIS.ST "\
"AFRY.ST "\
"LUMI.ST "\
"SUS.ST "\
"PDX.ST "\
"NEWA-B.ST "\
"NCC-B.ST "\
"SECARE.ST "\
"ARJO-B.ST "\
"ATRLJ-B.ST "\
"CORE-B.ST "\
"COOR.ST "\
"MEKO.ST "\
"BMAX.ST "\
"SDIP-B.ST "\
"IPCO.ST "\
"CATE.ST "\
"CALTX.ST "\
"TROAX.ST "\
"NOLA-B.ST "\
"LOGI-B.ST "\
"BUFAB.ST "\
"LAGR-B.ST "\
"SKIS-B.ST "\
"MTG-B.ST "\
"PEAB-B.ST "\
"MYCR.ST "\
"CLAS-B.ST "\
"SYNSAM.ST "\
"AOI.ST "\
"HMS.ST "\
"ANOD-B.ST "\
"BRAV.ST "\
"SVOL-B.ST "\
"BILI-A.ST "\
"BIOT.ST "\
"TOBII.ST "\
"RESURS.ST "\
"SCST.ST "\
"G5EN.ST "\
"RVRC.ST "\
"BONAV-B.ST "\
"GRNG.ST "\
"NOBI.ST "\
"BETCO.ST "\
"NCAB.ST "\
"VOLO.ST "\
"JOMA.ST "\
"INWI.ST "\
"EOLU-B.ST "\
"MTRS.ST "\
"HNSA.ST "\
"CRED-A.ST "\
"EXS.ST "\
"NOTE.ST "\
"NP3.ST "\
"GARO.ST "\
"BIOA-B.ST "\
"RENEW.ST "\
"FNM.ST "\
"OX2.ST "\
"CLA-B.ST "\
"SEYE.ST "\
"MCOV-B.ST "\
"EPRO-B.ST "\
"DSNO.ST "\
"COIC.ST "\
"COALA.ST "\
"ENQ.ST "\
"DUST.ST "\
"BALCO.ST "\
"TRANS.ST "\
"AMBEA.ST "\
"COLL.ST "\
"KNOW.ST "\
"TETY.ST "\
"SOLT.ST "\
"CAMX.ST "\
"ATT.ST "\
"AAC.ST "\
"ALIG.ST "\
"8TRA.ST "\
"ACAD.ST "\
"GENO.ST "\
"CANTA.ST "\
"BEIA-B.ST "\
"SIGNUP.ST "\
"BFG.ST "\
"FG.ST "\
"IVACC.ST "\
"EG7.ST "\
"SEDANA.ST "\
"ACCON.ST "\
"NWG.ST "\
"ACAST.ST "\
"XVIVO.ST "\
"OEM-B.ST "\
"BONEX.ST "\
"SIVE.ST "\
"THUNDR.ST "\
"AZELIO.ST "\
"CEVI.ST "\
"HANZA.ST "\
"BERG-B.ST "\
"TFBANK.ST "\
"ASAB.ST "\
"BRG-B.ST "\
"BULTEN.ST "\
"BIOG-B.ST "\
"BUSER.ST "\
"KFAST-B.ST "\
"IMP-A-SDB.ST "\
"FLAT-B.ST "\
"KAR.ST "\
"IMMNOV.ST "\
"DOXA.ST "\
"LUG.ST "\
"CS.ST "\
"GREEN.ST "\
"READ.ST "\
"PRIC-B.ST "\
"MAHA-A.ST "\
"HUM.ST "\
"BTS-B.ST "\
"FASTAT.ST "\
"STEF-B.ST "\
"FPIP.ST "\
"VEFAB.ST "\
"CAT-B.ST "\
"FAG.ST "\
"CDON.ST "\
"LINC.ST "\
"MCAP.ST "\
"HOFI.ST "\
"RAY-B.ST "\
"EAST.ST "\
"DUNI.ST "\
"IDUN-B.ST "\
"PLAZ-B.ST "\
"BEGR.ST "\
"AWRD.ST "\
"ENGCON-B.ST "\
"EQT.ST " \
"VPLAY-B.ST "\
"AQ.ST " \
"ARION-SDB.ST " \
"BACTI-B.ST " \
"BESQ.ST " \
"BRIN-B.ST " \
"CCC.ST " \
"COALA.ST " \
"CTT.ST " \
"ELAN-B.ST " \
"ELTEL.ST " \
"ENEA.ST " \
"FOI-B.ST " \
"HEBA-B.ST " \
"IAR-B.ST " \
"IVSO.ST " \
"LIME.ST " \
"LUC.ST " \
"MMGR-B.ST " \
"NMAN.ST " \
"NPAPER.ST " \
"ORES.ST " \
"PACT.ST " \
"PROB.ST " \
"QLINEA.ST " \
"REJL-B.ST " \
"RROS.ST " \
"SYSR.ST " \
"TIETOS.ST " \
"TRAC-B.ST " \
"TRIAN-B.ST " \
"VBG-B.ST " \
"XANO-B.ST " \
"XSPRAY.ST"


#=============================================================================
# ============================================================================
hist = yf.download(tickers, start='2015-01-01', end=tday_str)
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
vol_daily = ret_daily.rolling(60).std().shift(1)


#create binary dataframe to exclude stocks with big move large volume days in the last n sessions
long_ind = (r_vol > 3) & (ret_daily > 0) & (ret_daily < 0.08)
 
# #create position indicator df
# long_ind = significant_days.shift(1)

#long_ind = (ret_5d < 0) 
#replace false with NaN to avoid 0s impacting the mean
long_ind = long_ind.replace(False, np.nan)


short_ind =  (r_vol > 3.5) & (ret_daily < -0.1) & (ret_daily > -0.3)
short_ind = short_ind.replace(False, np.nan)



#calc transaction cost
n_trans = long_ind.sum().sum() #+ short_ind.sum().sum()

trans_value = n_trans*100000
total_trans_cost = n_trans*29

trans_proc_fee = total_trans_cost/trans_value


long_returns_daily = 1*(ret_daily-2*trans_proc_fee)*long_ind.shift(1)
short_returns_daily = -1*(ret_daily+2*trans_proc_fee)*short_ind.shift(1)


#daily returns of long short strategy
#avg_long_ret = starting_capital*long_returns_daily.mean(axis=1)-transaction_cost
avg_long_ret = long_returns_daily[long_returns_daily!=0].mean(axis=1)#-2*trans_proc_fee

#strat_vol = avg_long_ret.shift(1).rolling(20).std()

avg_short_ret = short_returns_daily[short_returns_daily!=0].mean(axis=1)#-2*trans_proc_fee
daily_returns_strat  =avg_long_ret.dropna(how='all').fillna(0) #+ avg_short_ret.dropna(how='all').fillna(0)#
daily_returns_strat = daily_returns_strat.fillna(0)
#avg_daily_rets  = daily_returns_strat.mean(axis=1)

#Cumulative returns 
#cum_ret =starting_capital +  np.cumsum(daily_returns_strat) #
cum_ret =(1 + daily_returns_strat).cumprod()
#cum_long_ret =  (1 + avg_long_ret).cumprod()
#cum_short_ret =  (1 + avg_short_ret).cumprod()

##########################################
#stats for basic strategy
##########################################

print("Basic strategy:   ")
print('Significant day effect ')
mean_ret = cum_ret.tail(1)**(1/8)-1
print("CAGR " + str(mean_ret[0]))
vol = (daily_returns_strat.std()*math.sqrt(252))
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

#calculate rolling sharpe ratio of basic strategy
#rolling_vol = daily_returns_strat.shift(1).rolling(100).std()
#rolling_return = cum_ret.pct_change(100).shift(1)
#strat_rolling_sharpe = rolling_return/rolling_vol

mom_cum_ret = (1+daily_returns_strat[cum_ret.pct_change(40).shift(1) > 0]).cumprod()
#mom_cum_ret =  (1+daily_returns_strat[strat_rolling_sharpe > 0.5]).cumprod()
#mom_cum_ret = starting_capital + np.cumsum(daily_returns_strat[cum_ret.pct_change(20).shift(1) > 0])
mom_daily_ret_RE = mom_cum_ret.pct_change()

mom_mean_ret = mom_cum_ret.tail(1)**(1/8)-1

mom_vol = (daily_returns_strat[cum_ret.pct_change(40).shift(1) > 0].std()*math.sqrt(252))
mom_sharpe = mom_mean_ret/mom_vol
mom_kelly_f = mom_mean_ret/mom_vol**2

#maxiumum drawdown
mom_Roll_Max = mom_cum_ret.cummax()
mom_Daily_Drawdown = mom_cum_ret/mom_Roll_Max - 1.0
mom_Max_Daily_Drawdown = mom_Daily_Drawdown.cummin()
print("   ")
print("Factor momentum:   ")
print('Significant day effect with momentum ')
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
boh_mean_ret = cum_ret_boh.tail(1)**(1/8)-1
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
print('40-day momentum of significant day effect strategy')
print(cum_ret.pct_change(40).tail(1))

