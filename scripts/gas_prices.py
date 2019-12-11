import urllib.request 
import json
import csv
from os import mkdir
from os.path import join, exists

import constants

data_dir = join('..', 'data') 
if not exists(data_dir):
    mkdir(data_dir)

series_dict = {
    constants.DAILY_SERIES_ID:'../data/daily_gas_prices.csv', 
    constants.WEEKLY_SERIES_ID:'../data/weekly_gas_prices.csv',
    constants.MONTHLY_SERIES_ID:'../data/monthly_gas_prices.csv',
    constants.ANNUAL_SERIES_ID:'../data/annual_gas_prices.csv'}

def toCSV(dataRows, csvFile):
    with open(csvFile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Date',  'Price(Dollars per Million Btu)'])
        writer.writerows(dataRows)

def makeDatapackage():
    f = open('../datapackage.json', 'w+')
    f.write(constants.DATAPACKAGE_JSON)
    f.close



for series_id, csvFileName in series_dict.items():
    request_url = urllib.request.urlopen(f'http://api.eia.gov/series/?api_key={constants.EIA_API_KEY}&series_id={series_id}') 
    data = json.loads(request_url.read().decode('utf8'))['series'][0]['data']
    toCSV(data, csvFileName)
    makeDatapackage()



