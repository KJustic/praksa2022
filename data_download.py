import requests
import datetime
import calendar
import os

# TAS,TASMIN,TASMAX DOWNLOAD FOR GCM='CN','EC','MP','HA' AND SCENARIOS 'historical','45','85'
start= datetime.datetime.now()

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
				
				x+=delta


print (datetime.datetime.now()-start)           
