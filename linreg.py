import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import geopandas as gpd
import os
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import datetime




LON =np.zeros(24)
LAT =np.zeros(24)
GRAD =[]
LON[0]=15.98; LAT[0]=45.81;   GRAD.append('Zagreb');
LON[1]=15.87; LAT[1]=46.16;   GRAD.append('Krapina'); 
LON[2]=16.36; LAT[2]=45.48;   GRAD.append('Sisak');
LON[3]=15.55; LAT[3]=45.48;   GRAD.append('Karlovac'); 
LON[4]=16.34; LAT[4]=46.31;   GRAD.append('Varaždin'); 
LON[5]=16.83; LAT[5]=46.16;   GRAD.append('Koprivnica'); 
LON[6]=16.84; LAT[6]=45.91;   GRAD.append('Bjelovar');
LON[7]=14.45; LAT[7]=45.33;   GRAD.append('Rijeka');
LON[8]=15.37; LAT[8]=44.54;   GRAD.append('Gospić');
LON[9]=17.40; LAT[9]=45.84;  GRAD.append('Virovitica');
LON[10]=17.67; LAT[10]=45.33; GRAD.append('Požega');
LON[11]=18.01; LAT[11]=45.16; GRAD.append('Slavonski_Brod');
LON[12]=15.23; LAT[12]=44.11; GRAD.append('Zadar');
LON[13]=18.70; LAT[13]=45.56; GRAD.append('Osijek');
LON[14]=15.89; LAT[14]=43.74; GRAD.append('Šibenik');
LON[15]=18.99; LAT[15]=45.35; GRAD.append('Vukovar');
LON[16]=16.44; LAT[16]=43.51; GRAD.append('Split');
LON[17]=13.94; LAT[17]=45.24; GRAD.append('Pazin');
LON[18]=18.11; LAT[18]=42.65; GRAD.append('Dubrovnik');
LON[19]=16.42; LAT[19]=46.39; GRAD.append('Čakovec');
LON[20]=17.48; LAT[20]=42.77; GRAD.append('Blato');
LON[21]=16.19; LAT[21]=44.04; GRAD.append('Knin');
LON[22]=16.64; LAT[22]=43.70; GRAD.append('Sinj');
LON[23]=14.98; LAT[23]=44.81; GRAD.append('Zavižan');


gcm=['CN','EC','MP','HA']

exp=['historical','45','85']

indeks=['_yearmean','_eca_su','_eca_csu','_eca_hwdi','_eca_hwfi']
imena = [['tas','tasmax','tasmin'],['summer_days_index_per_time_period',0,0],['consecutive_summer_days_index_per_time_period',0,0],['heat_wave_duration_index_wrt_mean_of_reference_period',0,0],['warm_spell_days_index_wrt_90th_percentile_of_reference_period',0,0]]


for n in range(0,len(indeks)):
	for k in range(0,len(imena[n])):
		if n==0:
			var=['tas','tasmax','tasmin']
		elif n in range(1,4):
			var=['tasmax','tasmax','tasmax']
		else:
			var=['tas','tas','tas']
		if imena[n][k] !=0:
			rezultat = np.zeros((2,4,24))
			for j in range(1,3):
				
				for i in range(0,4): 
					for l in range (0,24):		
						path = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
						ime = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
						
						out= path+GRAD[l]+'_'+ime+indeks[n]+'.nc'
						if os.path.exists(out):
							ds = nc.Dataset(out)
							nctime=ds['time'][:]
							t_cal=ds['time'].calendar
							data = ds.variables[imena[n][k]][:].flatten()
							time_var = ds.variables['time']
							t_unit = ds.variables['time'].units
							datevar = []
							datevar.append(nc.num2date(nctime,units = t_unit,calendar = t_cal,only_use_python_datetimes=True))
							time= [y for y in range(datevar[0][0].year,datevar[0][-1].year +1)]
							slope, intercept, r, p, se = stats.linregress(time, data)
							rezultat[j-1][i][l]=slope*10
			for j in range(1,3):
				plt.close('all')
				fig, ( (ax0, ax1),(ax2,ax3) ) = plt.subplots(2, 2,figsize=(20, 15))
				axs =[ax0,ax1,ax2,ax3]
				fig.suptitle('{} {}'.format(imena[n][k].replace('_', ' '), exp[j]),fontsize=25)
				worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
				 
				for i in range(0,4):
					if rezultat.any() != 0: 	
						output = '\n'.join('\t'.join(map(str,row)) for row in zip(GRAD,rezultat[j-1][i]))

						path1 = '/home/klara/Documents/praksa/podaci/{}/'.format(gcm[i])
						ime1 = '{}_CRO_{}_{}_{}_STS'.format(imena[n][k],gcm[i],exp[0],exp[j])
							
						out1= path1+ime1+'_linreg_slope.txt'
						with open(out1, 'w') as f:
	    						f.write(output)
						

						worldmap.plot(color="white",edgecolor='gray', ax=axs[i])
						x = LON
						y = LAT
						z = rezultat[j-1][i]
						graf=axs[i].scatter(x, y,s=70, c=z, alpha=0.6,cmap='autumn_r')
						cb=plt.colorbar(graf,fraction=0.03, ax=axs[i],format = "%0.1f")
						cb.set_label(label='{} \n rate of increase per 10 years '.format(imena[n][k].replace('_', ' ').capitalize() ), size=15)
						cb.ax.tick_params(labelsize='large')
						cb.mappable.set_clim(rezultat.min() , rezultat.max() ) 
						for m, label in enumerate(GRAD):
	    						axs[i].annotate(label, (x[m], y[m]),fontsize=8)
						axs[i].grid()
						axs[i].set_xlim([13.0, 20.0])
						axs[i].set_ylim([42.0, 47.0])
						axs[i].set_xlabel("Longitude",fontsize=15)
						axs[i].set_ylabel("Latitude",fontsize=15)
						axs[i].set_title("{}".format(gcm[i]),fontsize=20)
					plt.tight_layout()
					path2 = '/home/klara/Documents/praksa/linreg/'
					if not os.path.exists(path2):
						os.makedirs(path2)

					plt.savefig('{}{}_{}_slope.png'.format(path2,imena[n][k], exp[j]))
					
					
				
				
				
				
				
				
					
				
				
				
				
