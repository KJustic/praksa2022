import requests
import datetime
import calendar
import os
import numpy as np
import cdsapi
from zipfile import ZipFile
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# TAS,TASMIN,TASMAX DOWNLOAD FOR GCM='CN','EC','MP','HA' AND SCENARIOS 'historical','45','85'
start= datetime.datetime.now()

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


c = cdsapi.Client()
path='/home/klara/Documents/praksa/podaci_CLM_temporary/'
path2='/home/klara/Documents/praksa/podaci_CLM/'
path3='/home/klara/Documents/praksa/podaci_CLM_Croatia/'

if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(path2):
    os.makedirs(path2)
if not os.path.exists(path3):
    os.makedirs(path3)


c.retrieve(
    'projections-cordex-domains-single-levels',
    {
        'domain': 'europe',
        'experiment': 'historical',
        'horizontal_resolution': '0_11_degree_x_0_11_degree',
        'temporal_resolution': 'daily_mean',
        'variable': [
            '2m_air_temperature', 'maximum_2m_temperature_in_the_last_24_hours', 'minimum_2m_temperature_in_the_last_24_hours',
        ],
        'gcm_model': 'ichec_ec_earth',
        'rcm_model': 'clmcom_clm_cclm4_8_17',
        'ensemble_member': 'r12i1p1',
        'start_year': [
            '1971', '1976',
        ],
        'end_year': [
            '1975', '1980',
        ],
        'format': 'zip',
    },
    'download.zip')


with ZipFile('download.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(path)



for filename in os.listdir(path):
    f = os.path.join(path, filename)
    os.system("cdo sellonlatbox,13,20,42,47 {} {}".format(f,path3+"Croatia"+'_'+filename))
    for l in range (0,24):
    	os.system("cdo remapnn,lon={}_lat={}, {} {} ".format(LON[l],LAT[l],f,path2+GRAD[l]+'_'+filename))
    os.remove(f)
print (datetime.datetime.now()-start)      


