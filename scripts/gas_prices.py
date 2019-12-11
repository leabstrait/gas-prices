import urllib.request 
import json
import csv
from os import mkdir
from os.path import join, exists

import constants

# Make data directory
data_dir = join('..', 'data') 
if not exists(data_dir):
    mkdir(data_dir)

# Utility dict mapping API Params to data store locations
series_dict = {
    constants.DAILY_SERIES_ID:'../data/daily_gas_prices.csv', 
    constants.WEEKLY_SERIES_ID:'../data/weekly_gas_prices.csv',
    constants.MONTHLY_SERIES_ID:'../data/monthly_gas_prices.csv',
    constants.ANNUAL_SERIES_ID:'../data/annual_gas_prices.csv'}

# Write data to the provided CSV fle
def toCSV(dataRows, csvFile):
    header = ['Date',  'Price(Dollars per Million Btu)']
    with open(csvFile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(dataRows)

# Write the datapackage.json file
def makeDatapackage():
    f = open('../datapackage.json', 'w+')
    f.write(constants.DATAPACKAGE_JSON)
    f.close

def retrieve_uri_data(uri):
    resp = urllib.request.urlopen(uri)
    resp_data = json.loads(resp.read().decode('utf8'))
    return resp_data

# Fetch data and convert to CSV
def prepare_all_data():
    for series_id, csvFileName in series_dict.items():
        resp_data = retrieve_uri_data(f'http://api.eia.gov/series/?api_key={constants.EIA_API_KEY}&series_id={series_id}') 
        data = resp_data['series'][0]['data']
        toCSV(data, csvFileName)
        makeDatapackage()


if __name__ == '__main__':
    prepare_all_data()
