from os.path import join

# Key for U.S. Energy Information Administration API
EIA_API_KEY = 'a67246b03bbf71566663a8b5564f5d4c'

# API Param's IDs
DAILY_SERIES_ID = 'NG.RNGWHHD.D'                    # Henry Hub Natural Gas Spot Price, Daily
WEEKLY_SERIES_ID = 'NG.RNGWHHD.W'                   # Henry Hub Natural Gas Spot Price, Weekly
MONTHLY_SERIES_ID = 'NG.RNGWHHD.M'                  # Henry Hub Natural Gas Spot Price, Monthly
ANNUAL_SERIES_ID = 'NG.RNGWHHD.A'                   # Henry Hub Natural Gas Spot Price, Annual

# URIs for scraping
DAILY_SERIES_URI = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'      # Henry Hub Natural Gas Spot Price, Daily
WEEKLY_SERIES_URI = 'https://www.eia.gov/dnav/ng/hist/rngwhhdW.htm'     # Henry Hub Natural Gas Spot Price, Weekly
MONTHLY_SERIES_URI = 'https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm'    # Henry Hub Natural Gas Spot Price, Monthly
ANNUAL_SERIES_URI = 'https://www.eia.gov/dnav/ng/hist/rngwhhdA.htm'     # Henry Hub Natural Gas Spot Price, Annual

# Data Directory
DATA_DIR = join('..', 'data')

# Text Matter for datapackage.json
DATAPACKAGE_JSON = '''{
    "name": "gas-prices",
    "title": "Henry Hub Natural Gas Spot prices listed Daily, Weekly, Monthly and  Annually",
    "resources": [
        {
            "name": "api_daily_gas_prices",
            "path": "data/api_daily_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "api_weekly_gas_prices",
            "path": "data/api_weekly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "api_monthly_gas_prices",
            "path": "data/api_monthly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "api_annual_gas_prices",
            "path": "data/api_annual_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "scrape_daily_gas_prices",
            "path": "data/scrape_daily_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "scrape_weekly_gas_prices",
            "path": "data/scrape_weekly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "scrape_monthly_gas_prices",
            "path": "data/scrape_monthly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "scrape_annual_gas_prices",
            "path": "data/scrape_annual_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "name": "price",
                        "type": "float"
                    }
                ]
            }
        }
    ]
}
'''