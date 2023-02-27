import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime







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

tas_dhmz =[10.7,np.nan,11.0,np.nan,10.2,np.nan,np.nan,13.8, 8.7,np.nan,np.nan,10.7,14.9,11.0,np.nan,np.nan,16.1, 11.3,16.3,np.nan,np.nan,13.0,np.nan, 3.8]
tasmax_dhmz =[15.8,np.nan,16.0,np.nan,15.2,np.nan,np.nan,17.9,14.4,np.nan,np.nan,16.4, 18.9,16.5,np.nan,np.nan,19.4,18.0,19.7,np.nan,np.nan,19.1,np.nan,7.2]
tasmin_dhmz =[5.9,np.nan,5.9,np.nan,5.3,np.nan,np.nan,10.2,3.1,np.nan,np.nan,5.2,11.3,6.0,np.nan,np.nan,13.0,5.2,13.5,np.nan,np.nan,7.7,np.nan,1.1]
dhmz = ['tas dhmz','tasmax dhmz','tasmin dhmz']
var_dhmz =[tas_dhmz ,tasmax_dhmz,tasmin_dhmz]
gcm=['EC','MP','HA']

gcm_title=['ICHEC-EC-EARTH','MPI-M-MPI-ESM-LR','MOHC-HadGEM2-ES']
exp=['historical','45','85']
exp_title=['historical','rcp45','rcp85']
shade =['lightcoral', 'darkred']
indeks=['_yearmean','_eca_su','_eca_csu','_eca_hwdi','_eca_hwfi']
imena = [['tas','tasmax','tasmin'],['summer_days_index_per_time_period',0,0],['consecutive_summer_days_index_per_time_period',0,0],['heat_wave_duration_index_wrt_mean_of_reference_period',0,0],['warm_spell_days_index_wrt_90th_percentile_of_reference_period',0,0]]
naslov = [['tas [°C]','tasmax [°C]','tasmin [°C]'],['Indeks ljetnih dana po vremenskom razdoblju [dani] - ',0,0],['Indeks uzastopnih ljetnih dana \n po vremenskom razdoblju [dani] - ',0,0],['Indeks trajanja toplinskog vala u odnosu \n na srednju vrijednost referentnog razdoblja [dani] - ',0,0],['Indeks toplih dana u odnosu \n na 90. percentil referentnog razdoblja [dani] - ',0,0]]
"""
cols = ['Grad', 'gcm', 'var','exp','Climate indices','index','mean']
dat = pd.DataFrame(columns=cols)

for n in range(0,len(indeks)):
	for k in range(0,len(imena[n])):
		if n==0:
			var=['tas','tasmax','tasmin']
		elif n in range(1,4):
			var=['tasmax','tasmax','tasmax']
		else:
			var=['tas','tas','tas']
		if imena[n][k] !=0:
			rezultat = np.ndarray((2,24,3,100))
			sred= np.ndarray((2,24,3))
			for j in range(1,3):
			
				for l in range (0,24):
					
					#limit=[]
					for i in range(0,3): 
						path = '/media/sf_Documents/diplomski/podaci/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
						ime = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
						out= path+GRAD[l]+'_'+ime+indeks[n]+'.nc'
						out2= path + GRAD[l]+'_'+ime+indeks[n]+'_1971_2000' +'.nc'
						out3= path + GRAD[l]+'_'+ime+indeks[n]+ '_1971_2000_timmean' +'.nc'
						if os.path.exists(out2):
							os.system("rm -r {}".format(out2))
						if os.path.exists(out3):
							os.system("rm -r {}".format(out3))
						print(out)
						os.system("cdo selyear,1971/2000 {} {}".format(out,out2))
						os.system("cdo timmean {} {}".format(out2,out3))
						ds_mean = nc.Dataset(out3)
						ds_var = nc.Dataset(out)
						nctime=ds_var['time'][:]
						t_cal=ds_var['time'].calendar
						data = ds_var.variables[imena[n][k]][:].flatten()
						tmean = ds_mean.variables[imena[n][k]][:].flatten()
						time_var = ds_var.variables['time']
						t_unit = ds_var.variables['time'].units
						datevar = []
						datevar.append(nc.num2date(nctime,units = t_unit,calendar = t_cal,only_use_python_datetimes=True))
						time= [y for y in range(datevar[0][0].year,datevar[0][-1].year +1)]
						#limit.append(data)

						#rezultat[j-1][l][i][:]=data.tolist()
						sred[j-1][l][i]= tmean
						print(tmean)
						dat = dat.append({'Grad': GRAD[l], 'gcm': gcm[i], 'var': var[k],'exp': exp[j], 'Climate indices': indeks[n], 'index': imena[n][k],'mean': tmean -273.15},ignore_index=True)
						np.save('/media/sf_Documents/diplomski/rezultat_tmean_{}_{}_{}_{}_{}_regcm4'.format(exp[j],GRAD[l],gcm[i],imena[n][k],indeks[n]), data.tolist())
			np.save('/media/sf_Documents/diplomski/sred_tmean_{}_{}_regcm4'.format(imena[n][k],indeks[n]), sred)
dat.to_excel("/media/sf_Documents/diplomski/tmean_regcm4.xlsx")
		

"""			

for n in range(0,len(indeks)):
	for k in range(0,len(imena[n])):
		if n==0:
			var=['tas','tasmax','tasmin']
		elif n in range(1,4):
			var=['tasmax','tasmax','tasmax']
		else:
			var=['tas','tas','tas']
		if imena[n][k] !=0:		
			sred=np.load('/media/sf_Documents/diplomski/sred_tmean_{}_{}_regcm4.npy'.format(imena[n][k],indeks[n]))
			print(type(sred))
		
			for l in range (0,24):	
				plt.close('all')
				fig, axs = plt.subplots(3, 1,figsize=(12, 36))
				fig.suptitle('{} {} RegCM4'.format(GRAD[l],naslov[n][k].replace('_', ' ')),fontsize=30, wrap=True)
				limit=[]
				time=np.arange(1971,2071)
				for i in range(0,3): 
					for j in range(1,3):
						rezultat=np.load('/media/sf_Documents/diplomski/rezultat_tmean_{}_{}_{}_{}_{}_regcm4.npy'.format(exp[j],GRAD[l],gcm[i],imena[n][k],indeks[n]))
						print('/media/sf_Documents/diplomski/rezultat_tmean_{}_{}_{}_{}_{}_regcm4.npy'.format(exp[j],GRAD[l],gcm[i],imena[n][k],indeks[n]))
						if n==0:
							celz_rez = rezultat -273.15
							celz_sred = sred[j-1][l][i] -273.15
							axs[i].plot(time,celz_rez , label='{}'.format(exp_title[j]), color = '{}'.format(shade[j-1]))
							if j == 1:
								axs[i].axhline(celz_sred, label='srednjak modela 1971-2000', color = 'black')
								axs[i].axhline(var_dhmz[k][l], label='{} srednjak 1971-2000'.format(dhmz[k]), color = 'green')
							limitt = list(rezultat-273.15)
							if np.isnan(var_dhmz[k][l]) == False: 
								limitt.append(var_dhmz[k][l])	
							limit.append(limitt)

						else:
							axs[i].plot(time,rezultat, label='{}'.format(exp_title[j]),  color = '{}'.format(shade[j-1]))
							if j==1:
								axs[i].axhline(sred[j-1][l][i], label='srednjak modela 1971-2000', color = 'black')
							limit.append(rezultat)
						

				for i in range(0,3): 
					for ax in axs:
						ax.yaxis.set_tick_params(labelleft=True)
						
					axs[i].set_ylim(np.array(limit).min() , np.array(limit).max())
						
					axs[i].set_xlabel('Vrijeme [godine]',fontsize=20)

					axs[i].set_ylabel('{}'.format(naslov[n][k].replace('_', ' ').capitalize()),fontsize=20)
					
					axs[i].set_title('{}'.format(gcm_title[i]),fontsize=25)
					axs[i].legend(fontsize=15)
					path2 = '/media/sf_Documents/diplomski/tmean/'
					if not os.path.exists(path2):
						os.makedirs(path2)

					plt.savefig('{}{}_{}_tmean_RegCM4.png'.format(path2,GRAD[l],imena[n][k]))					
					
									

