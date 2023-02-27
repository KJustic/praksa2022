import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime
import pymannkendall as mk
from scipy import stats






GRAD =[]
GRAD.append('Zagreb');
GRAD.append('Krapina'); 
GRAD.append('Sisak');
GRAD.append('Karlovac'); 
GRAD.append('Varaždin'); 
GRAD.append('Koprivnica'); 
GRAD.append('Bjelovar');
GRAD.append('Rijeka');
GRAD.append('Gospić');
GRAD.append('Virovitica');
GRAD.append('Požega');
GRAD.append('Slavonski_Brod');
GRAD.append('Zadar');
GRAD.append('Osijek');
GRAD.append('Šibenik');
GRAD.append('Vukovar');
GRAD.append('Split');
GRAD.append('Pazin');
GRAD.append('Dubrovnik');
GRAD.append('Čakovec');
GRAD.append('Blato');
GRAD.append('Knin');
GRAD.append('Sinj');
GRAD.append('Zavižan');


gcm_reg=['EC','MP','HA']
var=['tas','tasmax','tasmin']
gcm_clm=['ICHEC-EC-EARTH','MOHC-HadGEM2-ES','MPI-M-MPI-ESM-LR']
exp_reg=['historical','45','85']
exp_clm=['historical','rcp45','rcp85']
shade =['light', 'dark']
color = ['green','red','blue']

indeks=['_yearmean','_eca_su','_eca_csu','_eca_hwdi','_eca_hwfi']
imena = [['tas','tasmax','tasmin'],['summer_days_index_per_time_period',0,0],['consecutive_summer_days_index_per_time_period',0,0],['heat_wave_duration_index_wrt_mean_of_reference_period',0,0],['warm_spell_days_index_wrt_90th_percentile_of_reference_period',0,0]]

cols = ['Grad', 'gcm', 'var','exp','Climate indices','index', 'variance', 'mean', 'lin_reg_slope', 'lin_reg_p', 'lin_reg_r', 'lin_reg_std_err', 'st_dev','mk_test_trend', 'mk_test_h', 'mk_test_p', 'mk_test_z', 'mk_test_Tau', 'mk_test_s', 'mk_test_var_s', 'mk_test_slope', 'mk_test_intercept']
dat_reg = pd.DataFrame(columns=cols)
dat_clm = pd.DataFrame(columns=cols)


for n in range(0,len(indeks)):
	for k in range(0,len(imena[n])):
		if n==0:
			var=['tas','tasmax','tasmin']
		elif n in range(1,4):
			var=['tasmax','tasmax','tasmax']
		else:
			var=['tas','tas','tas']
		if imena[n][k] !=0:
			for l in range (0,24):
				for i in range(0,3):
					for j in range(1,3):
						path_reg = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm_reg[i],var[k],exp_reg[j],exp_reg[0],GRAD[l])
						ime_reg = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm_reg[i],exp_reg[0],exp_reg[j])
						path_clm = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm_clm[i],var[k],exp_clm[j],exp_clm[0],GRAD[l])
						if i == 0:
							ime_clm= '{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm_clm[i],exp_clm[j],exp_clm[0])
						else:
							ime_clm= '{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm_clm[i],exp_clm[j],exp_clm[0])
						
						podatak_clm = path_clm+GRAD[l]+'_'+ime_clm+indeks[n]+'.nc'
						podatak_reg = path_reg+GRAD[l]+'_'+ime_reg+indeks[n]+'.nc'
						ds_reg = nc.Dataset(podatak_reg)
						ds_clm = nc.Dataset(podatak_clm)
						data_reg = ds_reg.variables[imena[n][k]][:].flatten()
						data_reg = list(data_reg.flatten()) 
						data_clm = ds_clm.variables[imena[n][k]][:].flatten()
						data_clm = list(data_clm.flatten()) 
						nctime_reg=ds_reg['time'][:].flatten()
						time_reg= np.arange(0,len(nctime_reg))
						nctime_clm=ds_clm['time'][:].flatten()
						time_clm= np.arange(0,len(nctime_clm))
						
						data_var_reg =np.var(data_reg)
						data_var_clm =np.var(data_clm)
						data_mean_reg =np.mean(data_reg)
						data_mean_clm =np.mean(data_clm)
						data_st_reg =np.std(data_reg)
						data_st_clm =np.std(data_clm)
						data_lr_s_reg, intercept_reg, data_lr_r_reg, data_lr_p_reg, data_lr_std_err_reg = stats.linregress(time_reg,data_reg)
						data_lr_s_clm, intercept_clm, data_lr_r_clm, data_lr_p_clm, data_lr_std_err_clm = stats.linregress(time_clm,data_clm)
						data_mk_reg_trend, data_mk_reg_h, data_mk_reg_p, data_mk_reg_z, data_mk_reg_Tau, data_mk_reg_s, data_mk_reg_var_s, data_mk_reg_slope, data_mk_reg_intercept = mk.original_test(data_reg)
						data_mk_clm_trend, data_mk_clm_h, data_mk_clm_p, data_mk_clm_z, data_mk_clm_Tau, data_mk_clm_s, data_mk_clm_var_s, data_mk_clm_slope, data_mk_clm_intercept= mk.original_test(data_clm)
						
						
						dat_reg = dat_reg.append({
						'Grad': GRAD[l], 
						'gcm': gcm_reg[i],
						'var': var[k],
						'exp': exp_reg[j], 
						'Climate indices': indeks[n],
						'index': imena[n][k],
						'variance': data_var_reg,
						'mean':data_mean_reg,
						'lin_reg_slope':data_lr_s_reg,
						'lin_reg_p':data_lr_p_reg,
						'lin_reg_r':data_lr_r_reg, 
						'lin_reg_std_err':data_lr_std_err_reg,
						'st_dev': data_st_reg,
						'mk_test_trend':data_mk_reg_trend, 
						'mk_test_h':data_mk_reg_h, 
						'mk_test_p':data_mk_reg_p, 
						'mk_test_z':data_mk_reg_z, 
						'mk_test_Tau':data_mk_reg_Tau, 
						'mk_test_s':data_mk_reg_s, 
						'mk_test_var_s':data_mk_reg_var_s,  
						'mk_test_slope':data_mk_reg_slope, 
						'mk_test_intercept':data_mk_reg_intercept},ignore_index=True)
						
						dat_clm= dat_clm.append({
						'Grad': GRAD[l], 
						'gcm': gcm_clm[i], 
						'var': var[k],
						'exp': exp_clm[j], 
						'Climate indices': indeks[n],
						'index': imena[n][k],
						'variance': data_var_clm, 
						'mean':data_mean_clm, 
						'lin_reg_slope':data_lr_s_clm,
						'lin_reg_p':data_lr_p_clm,
						'lin_reg_r':data_lr_r_clm,
						'lin_reg_std_err':data_lr_std_err_clm,
						'st_dev': data_st_clm,
						'mk_test_trend':data_mk_clm_trend, 
						'mk_test_h':data_mk_clm_h, 
						'mk_test_p':data_mk_clm_p, 
						'mk_test_z':data_mk_clm_z, 
						'mk_test_Tau':data_mk_clm_Tau, 
						'mk_test_s':data_mk_clm_s, 
						'mk_test_var_s':data_mk_clm_var_s, 
						'mk_test_slope':data_mk_clm_slope, 
						'mk_test_intercept':data_mk_clm_intercept},ignore_index=True)
						
dat_reg.to_excel("/home/klara/Documents/praksa/reg_temps_stat.xlsx")
dat_clm.to_excel("/home/klara/Documents/praksa/clm_temps_stat.xlsx")
