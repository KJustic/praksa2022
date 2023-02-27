
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

gcm=['ICHEC-EC-EARTH','MPI-M-MPI-ESM-LR','MOHC-HadGEM2-ES']
var=['tasmax']
exp=['historical','rcp45','rcp85']
shade =['lightcoral', 'darkred']

for l in range (0,24):
	plt.close('all')
	fig, axs = plt.subplots(3, 1,figsize=(12, 36), sharey=True)
	fig.suptitle('{} - CLM'.format(GRAD[l]),fontsize=30,wrap=True)
	fig1, axs1 = plt.subplots(3, 1,figsize=(12, 36), sharey=True)
	fig1.suptitle('{} - CLM'.format(GRAD[l]),fontsize=30,wrap=True)
	
	for i in range(0,3):
		for k in range(0,1):
			for j in range(1,3):
			
				path = '/media/sf_Documents/diplomski/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				path2 = '/media/sf_Documents/diplomski/podaci_CLM/{}/{}_{}_{}/{}/selyear/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				path3 = '/media/sf_Documents/diplomski/podaci_CLM/{}/{}_{}_{}/{}/splityear/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				if not os.path.exists(path2):
					os.makedirs(path2)
				if not os.path.exists(path3):
					os.makedirs(path3)
				if i == 0:
					ime = '{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[0])
				else:
					ime = '{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[0])
				"""
				out = path+GRAD[l]+'_'+ime+'.nc'
				out2= path2 + '1971_2000' +'.nc'
				out3= path2 + 'ydrunmean' +'.nc'
				ifile2= path + 'JJA_runmean' +'.nc'
				os.system("cdo selyear,1971/2000 {} {}".format(out,out2))
				os.system("cdo ydrunmean,5 {} {}".format(out2,out3))
				os.system("cdo selseas,JJA {} {}".format(out3,ifile2))
				os.system("rm -r {}".format(path2))
				os.system("cdo splityear {} {}".format(out,path3))
				for m in range(1971,2071):
					ime2 = '{}'.format(m)
					out2= path3 + ime2 +'.nc'
					out3= path3 +'eca_hwdi_'+ ime2 +'.nc'
					ifile1 = path + 'JJA' + '.nc'
					os.system("cdo selseas,JJA {} {}".format(out2,ifile1))
					os.system("cdo eca_hwdi {} {} {}".format(ifile1, ifile2, out3))
				out4= path3 +'eca_hwdi_'
				"""
				out5= path + GRAD[l]+'_'+ime+ '_eca_hwdi'+'.nc'
				"""
				if os.path.exists(out5):
					os.system("rm -r {}".format(out5))
				os.system("cdo mergetime {}*.nc {}".format(out4,out5))
				os.system("rm -r {}".format(path3))
				"""
				ds = nc.Dataset(out5)
				nctime=ds['time'][:]
				t_cal=ds['time'].calendar
				mref = ds.variables['heat_wave_duration_index_wrt_mean_of_reference_period'][:].flatten()
				ptp = ds.variables['heat_waves_per_time_period'][:].flatten()
				time_var = ds.variables['time']
				t_unit = ds.variables['time'].units
				datevar = []
				datevar.append(nc.num2date(nctime,units = t_unit,calendar = t_cal,only_use_python_datetimes=True))
				time= [y for y in range(datevar[0][0].year,datevar[0][-1].year +1)]
				axs = axs.flatten()
				axs[i].plot(time,mref, label='{} {}'.format(var[k],exp[j]), color = '{}'.format(shade[j-1]))
				axs1 = axs1.flatten()
				axs1[i].bar(time,ptp, label='{} {}'.format(var[k],exp[j]), color = '{}'.format(shade[j-1]))
		
		for ax in axs.flatten():
			ax.yaxis.set_tick_params(labelleft=True)
		for ax in axs1.flatten():
			ax.yaxis.set_tick_params(labelleft=True)
    		
		axs[i].set_ylim([-5, 90])
		axs1[i].set_ylim([0, 7])	
		axs[i].set_xlabel('Vrijeme [godine]',fontsize=20)
		axs1[i].set_xlabel('Vrijeme [godine]',fontsize=20)

		axs[i].set_ylabel('Indeks trajanja toplinskog vala u odnosu na \n srednju vrijednost referentnog razdoblja [dani]',fontsize=20)
		axs1[i].set_ylabel('Toplinski valovi po vremenskom razdoblju',fontsize=20)
		axs[i].set_title('{}'.format(gcm[i]),fontsize=25)
		axs[i].legend(fontsize=15)
		axs1[i].set_title('{}'.format(gcm[i]),fontsize=25)
		axs1[i].legend(fontsize=15)

	path3 = '/media/sf_Documents/diplomski/eca_hwdi_CLM/'
	if not os.path.exists(path3):
		os.makedirs(path3)
	fig.savefig('{}{}_heat_wave_duration_index_CLM.png'.format(path3,GRAD[l]))
	fig1.savefig('{}{}_heat_waves_CLM.png'.format(path3,GRAD[l]))
					
				
				
				
