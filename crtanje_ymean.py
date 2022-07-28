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
GRAD.append('Knin');
GRAD.append('Sinj');
GRAD.append('Zavižan');

gcm=['CN','EC','MP','HA']
var=['tas','tasmax','tasmin']
exp=['historical','45','85']
shade =['light', 'dark']
color = ['green','red','blue']
for l in range (0,24):
	plt.close('all')
	fig, axs = plt.subplots(2, 2,figsize=(15, 15), sharey=True)
	fig.suptitle('{}'.format(GRAD[l]),fontsize=25)
	for i in range(0,4):
		for k in range(0,3):
			for j in range(1,3):
				path = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				ime = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
				out = path+GRAD[l]+'_'+ime+'.nc'
				out2 = path+GRAD[l]+'_'+ime+ '_yearmean'+'.nc'
				os.system("cdo yearmean {} {}".format(out,out2))

				ds = nc.Dataset(out2)

				nctime=ds['time'][:]
				t_cal=ds['time'].calendar
				data = ds.variables[var[k]][:].flatten()
				time_var = ds.variables['time']
				t_unit = ds.variables['time'].units
				datevar = []
				datevar.append(nc.num2date(nctime,units = t_unit,calendar = t_cal,only_use_python_datetimes=True))
				time= [y for y in range(datevar[0][0].year,datevar[0][-1].year +1)]
				axs = axs.flatten()
				if k==1 and j==1:
					axs[i].plot(time,data-273.15, label='{} {}'.format(var[k],exp[j]), color = '{}{}'.format(shade[j-1],'coral'))
				else:

					axs[i].plot(time,data-273.15, label='{} {}'.format(var[k],exp[j]), color = '{}{}'.format(shade[j-1],color[k]))

		for ax in axs.flatten():
			ax.yaxis.set_tick_params(labelleft=True)
		
		axs[i].set_ylim([0, 25])
		axs[i].set_xlabel('Time [years]',fontsize=15)
		axs[i].tick_params(axis='x', labelsize= 10)
		axs[i].tick_params(axis='y', labelsize= 10)
		axs[i].set_ylabel('Temperature [°C]',fontsize=15)
		
		axs[i].set_title('{}'.format(gcm[i]),fontsize=20)
		axs[i].legend()
	path2 = '/home/klara/Documents/praksa/ymean/'
	if not os.path.exists(path2):
		os.makedirs(path2)

	plt.savefig('{}{}_yearmean.png'.format(path2,GRAD[l]))
					
