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
var=['tas','tasmax','tasmin']
exp=['historical','45','85']

for l in range (0,21):
	plt.close('all')
	fig, axs = plt.subplots(2, 2,figsize=(15, 15))
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
				axs[i].plot(time,data, label='{} {}'.format(var[k],exp[j]))
		
		axs[i].set_title('{}'.format(gcm[i]),fontsize=20)
		axs[i].legend()
	

		for ax in axs.flat:
	    		ax.set(xlabel='time', ylabel='temperature [K]')


		for ax in axs.flat:
	    		ax.label_outer()


	fig.subplots_adjust(wspace=0.01, hspace=0.1)
	plt.savefig('{}_yearmean.png'.format(GRAD[l]))
					
