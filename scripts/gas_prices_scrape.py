import urllib.request
from bs4 import BeautifulSoup
import csv

import constants
from utils import make_data_dir, toCSV, makeDatapackage

# Name of files to store CSV data on
csv_file_daily   = constants.DATA_DIR + '/scrape_daily_gas_prices.csv' 
csv_file_weekly  = constants.DATA_DIR + '/scrape_weekly_gas_prices.csv'
csv_file_monthly = constants.DATA_DIR + '/scrape_monthly_gas_prices.csv'
csv_file_annual  = constants.DATA_DIR + '/scrape_annual_gas_prices.csv'

# DAILY
# =====================================================================================

def month_num(month_str):
    nums = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12,
    }
    return nums.get(month_str.lower())

def scrape_daily_data():
    resp = urllib.request.urlopen(constants.DAILY_SERIES_URI)
    resp_data = resp.read()

    soup = BeautifulSoup(resp_data, 'html.parser')
    data_table = soup.find_all('table')[5]

    all_weeks = data_table.find_all('td', {"class": "B6"})
    all_prices  = data_table.find_all('td', {"class": "B3"})


    records = []
    for week in all_weeks:
        day = 0
        
        for price in all_prices:
            week_string = week.string.strip()
            date = ( week_string[:4]                        +
                     '-'                                    +
                     f'{month_num(week_string[5:8]):02}'    +
                    '-'                                     +
                     f'{(int(week_string[9:11]) + day):02}'
                    )
            
            day = day + 1
            records.append([date, price.string])

            if day >= 5:
                all_prices = all_prices[5:]
                break
        
    toCSV(records, csv_file_daily)

# WEEKLY
# =====================================================================================

def scrape_weekly_data():

    resp = urllib.request.urlopen(constants.WEEKLY_SERIES_URI)
    resp_data = resp.read()

    soup = BeautifulSoup(resp_data, 'html.parser')
    data_table = soup.find_all('table')[4]

    all_years_months = data_table.find_all('td', {"class": "B6"})
    all_weekend_dates = data_table.find_all('td', {"class": "B5"})
    all_prices  = data_table.find_all('td', {"class": "B3"})

    records = []
    for year_month in all_years_months:        
        week = 1
        year_month_string = year_month.string.strip()

        for weekend_date in all_weekend_dates:
            weekend_date_string = weekend_date.string.strip()

            if not (len(weekend_date_string)==0):
                date = (year_month_string[:4]   +
                        '-'                     +
                        weekend_date_string.replace('/','-'))
                records.append([date, all_prices[week-1].string.strip()])

            week = week + 1

            if week > 5:
                all_weekend_dates = all_weekend_dates[5:]
                all_prices = all_prices[5:]
                break
        
    toCSV(records, csv_file_weekly)

# MONTHLY
# =====================================================================================

def scrape_monthly_data():

    resp = urllib.request.urlopen(constants.MONTHLY_SERIES_URI)
    resp_data = resp.read()

    soup = BeautifulSoup(resp_data, 'html.parser')
    data_table = soup.find_all('table')[4].find('table')

    all_years = data_table.find_all('td', {"class": "B4"})
    all_prices  = data_table.find_all('td', {"class": "B3"})

    records = []
    for year in all_years:
        month = 1
        for price in all_prices:            
            date = year.string.strip() + '-' + f'{month:02}' + '-' + '01'
            
            month = month + 1
            records.append([date, price.string])

            if month > 12:
                all_prices = all_prices[12:]
                break
        
    toCSV(records, csv_file_monthly)

# ANNUAL
# =====================================================================================

def scrape_annual_data():

    resp = urllib.request.urlopen(constants.ANNUAL_SERIES_URI)
    resp_data = resp.read()

    soup = BeautifulSoup(resp_data, 'html.parser')
    data_table = soup.find_all('table')[5]

    all_decades = data_table.find_all('td', {"class": "B4"})
    all_prices  = data_table.find_all('td', {"class": "B3"})

    records = []
    for decade in all_decades:
        year = 0
        for price in all_prices:
            decade_prefix = int(decade.string.strip()[:3])
            date = str(decade_prefix) + str(year)
            
            year = year + 1
            records.append([date, price.string])

            if year > 9:
                all_prices = all_prices[10:]
                break
        
    toCSV(records, csv_file_annual)


if __name__ == '__main__':
    scrape_daily_data()
    scrape_weekly_data()
    scrape_monthly_data()
    scrape_annual_data()

    makeDatapackage()
