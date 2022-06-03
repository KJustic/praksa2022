import os
import numpy as np
import matplotlib.pyplot as plt
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

gcm=['CN','EC','MP','HA']
var=['tas']
exp=['historical','45','85']
shade =['lightcoral', 'darkred']

for l in range (0,21):
	plt.close('all')
	fig, axs = plt.subplots(2, 2,figsize=(15, 15), sharey=True)
	fig.suptitle('{}'.format(GRAD[l]),fontsize=25)
	fig1, axs1 = plt.subplots(2, 2,figsize=(15, 15), sharey=True)
	fig1.suptitle('{}'.format(GRAD[l]),fontsize=25)
	
	for i in range(0,4):
		for k in range(0,1):
			for j in range(1,3):
			
				path = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				path2 = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/selyear/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				path3 = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/splityear/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				if not os.path.exists(path2):
					os.makedirs(path2)
				if not os.path.exists(path3):
					os.makedirs(path3)
				ime = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
				out = path+GRAD[l]+'_'+ime+'.nc'
				out2= path2 + '1970_2000' +'.nc'
				out3= path2 + 'ydrunpctl' +'.nc'
				ifile2= path + 'JJA_runpctl' +'.nc'
				os.system("cdo selyear,1970/2000 {} {}".format(out,out2))
				os.system("cdo ydrunpctl,90,5 {} -ydrunmin,5 {} -ydrunmax,5 {} {}".format(out2,out2,out2, out3))
				os.system("cdo selseas,JJA {} {}".format(out3,ifile2))
				os.system("rm -r {}".format(path2))
				os.system("cdo splityear {} {}".format(out,path3))
				for m in range(1970,2071):
					ime2 = '{}'.format(m)
					out2= path3 + ime2 +'.nc'
					out3= path3 +'eca_hwfi_'+ ime2 +'.nc'
					ifile1 = path + 'JJA' + '.nc'
					os.system("cdo selseas,JJA {} {}".format(out2,ifile1))
					os.system("cdo eca_hwfi {} {} {}".format(ifile1, ifile2, out3))
				out4= path3 +'eca_hwfi_'
				out5= path + GRAD[l]+'_'+ime+ '_eca_hwfi'+'.nc'
				if os.path.exists(out5):
					os.system("rm -r {}".format(out5))
				
				os.system("cdo mergetime {}*.nc {}".format(out4,out5))
				os.system("rm -r {}".format(path3))
				ds = nc.Dataset(out5)

				nctime=ds['time'][:]
				t_cal=ds['time'].calendar
				index = ds.variables['warm_spell_days_index_wrt_90th_percentile_of_reference_period'][:].flatten()
				ptp = ds.variables['warm_spell_periods_per_time_period'][:].flatten()
				time_var = ds.variables['time']
				t_unit = ds.variables['time'].units
				datevar = []
				datevar.append(nc.num2date(nctime,units = t_unit,calendar = t_cal,only_use_python_datetimes=True))
				time= [y for y in range(datevar[0][0].year,datevar[0][-1].year +1)]
				axs = axs.flatten()
				axs[i].plot(time,index, label='{} {}'.format(var[k],exp[j]), color = '{}'.format(shade[j-1]))
				axs1 = axs1.flatten()
				axs1[i].bar(time,ptp, label='{} {}'.format(var[k],exp[j]), color = '{}'.format(shade[j-1]))
				
		
		for ax in axs.flatten():
			ax.yaxis.set_tick_params(labelleft=True)
		for ax in axs1.flatten():
    			ax.yaxis.set_tick_params(labelleft=True)
    			
		axs[i].set_xlabel('time')
		axs1[i].set_xlabel('time')

		axs[i].set_ylabel('warm spell days index')
		axs1[i].set_ylabel('warm spell periods')
		axs[i].set_title('{}'.format(gcm[i]),fontsize=20)
		axs[i].legend()
		axs1[i].set_title('{}'.format(gcm[i]),fontsize=20)
		axs1[i].legend()

	path3 = '/home/klara/Documents/praksa/eca_hwfi/'
	if not os.path.exists(path3):
		os.makedirs(path3)
	fig.savefig('{}{}_warm_spell_days_index.png'.format(path3,GRAD[l]))
	fig1.savefig('{}{}_warm_spell_periods.png'.format(path3,GRAD[l]))
					
				
				
				
