import urllib.request 
import json
import csv

import constants
from utils import make_data_dir, toCSV, makeDatapackage

# Utility dict mapping API Params to data store locations
series_dict = {
    constants.DAILY_SERIES_ID:      constants.DATA_DIR + '/api_daily_gas_prices.csv', 
    constants.WEEKLY_SERIES_ID:     constants.DATA_DIR + '/api_weekly_gas_prices.csv',
    constants.MONTHLY_SERIES_ID:    constants.DATA_DIR + '/api_monthly_gas_prices.csv',
    constants.ANNUAL_SERIES_ID:     constants.DATA_DIR + '/api_annual_gas_prices.csv'
}


def retrieve_uri_data(uri):
    resp = urllib.request.urlopen(uri)
    resp_data = json.loads(resp.read().decode('utf8'))
    return resp_data

# Fetch data and convert to CSV
def prepare_all_data():
    for series_id, csv_file_name in series_dict.items():
        resp_data = retrieve_uri_data(f'http://api.eia.gov/series/?api_key={constants.EIA_API_KEY}&series_id={series_id}') 
        data = resp_data['series'][0]['data']
        toCSV(data, csv_file_name)


if __name__ == '__main__':
    make_data_dir()
    prepare_all_data()
    makeDatapackage()