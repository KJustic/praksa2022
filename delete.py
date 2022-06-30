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

for l in range (21,24):
	for i in range(0,4):
		for k in range(0,3):
			for j in range(0,3):
				path = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
				path1 = '/home/klara/Documents/praksa/podaci/{}/{}_{}/{}/'.format(gcm[i],var[k],exp[j],GRAD[l])
				if os.path.exists(path):
					os.system("rm -r {}".format(path))
				if os.path.exists(path1):
					os.system("rm -r {}".format(path1))
				
				
				
				
				
