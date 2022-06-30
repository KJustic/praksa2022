import matplotlib.pyplot as plt

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



gcm=['CN','EC','MP','HA']

exp=['historical','45','85']

indeks=['_yearmean','_eca_su','_eca_csu','_eca_hwdi','_eca_hwfi']
imena = [['tas','tasmax','tasmin'],['summer_days_index_per_time_period',0,0],['consecutive_summer_days_index_per_time_period',0,0],['heat_wave_duration_index_wrt_mean_of_reference_period',0,0],['warm_spell_days_index_wrt_90th_percentile_of_reference_period',0,0]]

for l in range (0,24):
	for n in range(0,len(indeks)):
		for j in range(1,3):
			for k in range(0,len(imena[n])):
				if n==0:
					var=['tas','tasmax','tasmin']
				elif n in range(1,4):
					var=['tasmax','tasmax','tasmax']
				else:
					var=['tas','tas','tas']
				if imena[n][k] !=0:
					plt.close('all')
					fig, ( (ax0, ax1),(ax2,ax3) ) = plt.subplots(2, 2,figsize=(20, 20))
					axs =[ax0,ax1,ax2,ax3]
					fig.suptitle('{} {} {}'.format(GRAD[l],imena[n][k].replace('_', ' '), exp[j]),fontsize=25)
					for i in range(0,4): 
						path = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
						ime = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
						
						out= path+GRAD[l]+'_'+ime+indeks[n]+'.nc'
						out2= path + GRAD[l]+'_'+ime+indeks[n]+'_1970_2000' +'.nc'
						out3= path + GRAD[l]+'_'+ime+indeks[n]+ '_1970_2000_timmean' +'.nc'
			
						os.system("cdo selyear,1970/2000 {} {}".format(out,out2))
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
						
						axs[i].plot(time,data, label='{}'.format(imena[n][k].replace('_', ' ')), color = 'red')
						axs[i].axhline(tmean, label='{} mean 1970-2000'.format(imena[n][k].replace('_', ' ')), color = 'black')
		
						for ax in axs:
							ax.yaxis.set_tick_params(labelleft=True)
							
						#axs[i].set_ylim([0, 175])
						axs[i].set_xlabel('time',fontsize=15)

						axs[i].set_ylabel('{}'.format(imena[n][k].replace('_', ' ')),fontsize=15)
						
						axs[i].set_title('{}'.format(gcm[i]),fontsize=20)
						axs[i].legend()
					path2 = '/home/klara/Documents/praksa/tmean/'
					if not os.path.exists(path2):
						os.makedirs(path2)

					plt.savefig('{}{}_{}_{}_tmean.png'.format(path2,GRAD[l],imena[n][k], exp[j]))
					
					
					
