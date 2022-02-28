import requests
import datetime
import calendar
import os

# TAS HA DOWNLOAD za rcp4.5 
link = 'https://repozitorij.meteo.hr/data/refolder4-2017-lvl1/RES_12/folder_HA/EXP_rcp45/tas_CRO_HA_45_STS.'    
x=datetime.date(2005,12,1)
datum=datetime.date(2070,12,1)

while x<=datum:
    	day_in_mon=calendar.monthrange(x.year,x.month)[1]
    	delta=datetime.timedelta(days=day_in_mon)
    	print(x)
    	dat=x.strftime('%Y')+x.strftime('%m')+x.strftime('%d')
    	url=link+dat+'00.nc'
    	data = requests.get(url, allow_redirects=True)
    	ime='tas_CRO_HA_45_STS.'
    	path='/home/klara/Documents/praksa/podaci/HA/tas_45/'
    	if not os.path.exists(path):
    		os.makedirs(path)
    	open(path+ime+dat+'00.nc', 'wb').write(data.content)
                
    	x+=delta
    	
    	

