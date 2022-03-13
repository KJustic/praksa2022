import requests
import datetime
import calendar
import os
import numpy as np

# TAS,TASMIN,TASMAX DOWNLOAD FOR GCM='CN','EC','MP','HA' AND SCENARIOS 'historical','45','85'
start= datetime.datetime.now()

LON =np.zeros(21)
LAT =np.zeros(21)
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

gcm=['CN','EC','MP','HA']
var=['tas','tasmax','tasmin']
exp=['historical','45','85']
for i in range(0,4):
	for j in range(0,3):
		for k in range(0,3):
			if exp[j] == 'historical':
				link = 'https://repozitorij.meteo.hr/data/regcm4-2017-lvl1/RES_12/GCM_{}/EXP_{}/{}_CRO_{}_STS.'.format(gcm[i],exp[j],var[k],gcm[i])
				x=datetime.date(1970,1,1)
				datum=datetime.date(2005,11,1)
				
			else:
				link = 'https://repozitorij.meteo.hr/data/regcm4-2017-lvl1/RES_12/GCM_{}/EXP_rcp{}/{}_CRO_{}_{}_STS.'.format(gcm[i],exp[j],var[k],gcm[i],exp[j])
				x=datetime.date(2005,12,1)
				datum=datetime.date(2070,12,1)
			
			
			while x<=datum:
				dan=calendar.monthrange(x.year,x.month)[1]
				delta=datetime.timedelta(days=dan)
				print(x)
				dat=x.strftime('%Y')+x.strftime('%m')+x.strftime('%d')
				url=link+dat+'00.nc'
				data = requests.get(url, allow_redirects=True)
				ime='{}_CRO_{}_{}_STS.'.format(var[k],gcm[i],exp[j])
				path='/home/klara/Documents/praksa/podaci/{}/{}_{}/'.format(gcm[i],var[k],exp[j])
				if not os.path.exists(path):
					os.makedirs(path)
				open(path+ime+dat+'00.nc', 'wb').write(data.content)
				for l in range (0,21):
					os.system("cdo remapnn,lon={}_lat={}, {} {} ".format(LON[l],LAT[l],path+ime+dat+'00.nc',path+GRAD[l]+'_'+ime+dat+'00.nc'))
					#print("cdo remapnn,lon={}_lat={}, {} {} ".format(LON[l],LAT[l],path+ime+dat+'00.nc',path+GRAD[l]+'_'+ime+dat+'00.nc'))
				os.remove(path+ime+dat+'00.nc')
				x+=delta
			

print (datetime.datetime.now()-start)      

