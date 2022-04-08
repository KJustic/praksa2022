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
			for l in range (0,21):
				path2 = '/home/klara/Documents/praksa/podaci/{}/{}_{}/{}/'.format(gcm[i],var[k],exp[j],GRAD[l])
				path3 = '/home/klara/Documents/praksa/podaci/{}/{}_{}/{}/'.format(gcm[i],var[k],exp[0],GRAD[l])
				ime= '{}_CRO_{}_{}_STS'.format(var[k],gcm[i],exp[j])
				ime2 ='{}_CRO_{}_{}_STS'.format(var[k],gcm[i],exp[0])
				out = path2+GRAD[l]+'_'+ime+'.nc'
				out2 = path3+GRAD[l]+'_'+ime2+'.nc'
				os.system("cdo mergetime {}*.nc {}".format(path2, out))
				#os.system("rm {}".format(out))

				if (j > 0):
					path4 = '/home/klara/Documents/praksa/podaci/{}/{}_{}_{}/{}/'.format(gcm[i],var[k],exp[j],exp[0],GRAD[l])
					if not os.path.exists(path4):
						os.makedirs(path4)
					ime3 = '{}_CRO_{}_{}_{}_STS'.format(var[k],gcm[i],exp[0],exp[j])
					out3 = path4+GRAD[l]+'_'+ime3+'.nc'
					os.system("cdo copy {} {} {}".format(out2,out, out3))
					print(out2,out, out3)
	'''	
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
					os.system("cdo shifttime,-1hours {} {}".format(path2+GRAD[l]+'_'+ime+dat+'00.nc', path2+GRAD[l]+'_'+ime+dat+'00.nc'))
					print(path2+GRAD[l]+'_'+ime+dat+'00.nc', path2+GRAD[l]+'_'+ime+dat+'00.nc')
					
				x+=delta
				

			
		'''
			

			
