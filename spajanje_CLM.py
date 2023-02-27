import requests
import datetime
import calendar
import os
import numpy as np
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



gcm=['ICHEC-EC-EARTH','MOHC-HadGEM2-ES','MPI-M-MPI-ESM-LR']
var=['tas','tasmax','tasmin']
exp=['historical','rcp45','rcp85']
"""
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			for l in range (0,24):		
				path = '/home/klara/Documents/praksa/podaci_CLM/'
				
				path2 = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[j],GRAD[l])
				
				if not os.path.exists(path2):
						os.makedirs(path2)
				
				ime= '{}_EUR-11_{}_{}'.format(var[k],gcm[i],exp[j])
				ime_his='{}_EUR-11_{}_{}'.format(var[k],gcm[i],exp[j])
				if i == 0:
					ime2 = '{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[j])
				else:
					ime2 = '{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[j])
				inpath = path+GRAD[l]+'_'+ime
				out = path2+GRAD[l]+'_'+ime2+'.nc'
				
				os.system("cdo mergetime {}*.nc {}".format(inpath, out))

for i in range(0,3):
	for j in range(1,3):
		for k in range(0,3):
			for l in range (0,24):		
				
				path = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[j],GRAD[l])
				path2 = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[0],exp[0],GRAD[l])
				path3 = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				if not os.path.exists(path3):
					os.makedirs(path3)
				
				if i == 0:
					ime= '{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[j])
					ime_his='{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[0],exp[0])
					ime2 = '{}_EUR-11_{}_{}_{}_r12i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[0])
				else:
					ime= '{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[j])
					ime_his='{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[0],exp[0])
					ime2 = '{}_EUR-11_{}_{}_{}_r1i1p1_CLMcom-CCLM4-8-17_v1_day'.format(var[k],gcm[i],exp[j],exp[0])
				inpath = path+GRAD[l]+'_'+ime+'.nc'
				inpath2 = path2+GRAD[l]+'_'+ime_his+'.nc'
				out = path3+GRAD[l]+'_'+ime2+'.nc'
				if os.path.exists(path3):
					os.system("rm {}".format(out))
				
				os.system("cdo mergetime {} {} {}".format(inpath, inpath2, out))			
"""
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			for l in range (0,24):	
				path = '/home/klara/Documents/praksa/podaci_CLM/'
				path3 = '/home/klara/Documents/praksa/podaci_CLM/{}/{}_{}/{}/'.format(gcm[i],var[k],exp[j],GRAD[l])
				if not os.path.exists(path3):
					os.makedirs(path3)
				ime= '{}_EUR-11_{}_{}'.format(var[k],gcm[i],exp[j])
				inpath = path+GRAD[l]+'_'+ime
				os.system("mv {}*.nc {}".format(inpath, path3))
				
