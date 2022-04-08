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

gcm=['CN','EC','MP','HA']
var=['tas','tasmax','tasmin']
exp=['historical','45','85']
for i in range(0,4):
	for j in range(0,3):
		for k in range(0,3):
			if exp[j] == 'historical':
				x=datetime.date(1970,1,1)
				datum=datetime.date(2005,11,1)
				
			else:
				x=datetime.date(2005,12,1)
				datum=datetime.date(2070,12,1)
			
			
			while x<=datum:
				dan=calendar.monthrange(x.year,x.month)[1]
				delta=datetime.timedelta(days=dan)
				print(x)
				dat=x.strftime('%Y')+x.strftime('%m')+x.strftime('%d')
				ime='{}_CRO_{}_{}_STS.'.format(var[k],gcm[i],exp[j])
				path='/home/klara/Documents/praksa/podaci/{}/{}_{}/'.format(gcm[i],var[k],exp[j])
			
				for l in range (0,21):
					path2 = path+'{}/'.format(GRAD[l])
					print(path2)
					if not os.path.exists(path2):
						os.makedirs(path2)
					os.system("mv {}  {} ".format(path+GRAD[l]+'_'+ime+dat+'00.nc', path2+GRAD[l]+'_'+ime+dat+'00.nc') )
					print(path+GRAD[l]+'_'+ime+dat+'00.nc', path2+GRAD[l]+'_'+ime+dat+'00.nc')
				x+=delta

