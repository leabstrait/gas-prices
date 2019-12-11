# Key for U.S. Energy Information Administration API
EIA_API_KEY = 'a67246b03bbf71566663a8b5564f5d4c'

# API Prams IDs
DAILY_SERIES_ID = 'NG.RNGWHHD.D'                    # Henry Hub Natural Gas Spot Price, Daily
WEEKLY_SERIES_ID = 'NG.RNGWHHD.W'                   # Henry Hub Natural Gas Spot Price, Weekly
MONTHLY_SERIES_ID = 'NG.RNGWHHD.M'                  # Henry Hub Natural Gas Spot Price, Monthly
ANNUAL_SERIES_ID = 'NG.RNGWHHD.A'                   # Henry Hub Natural Gas Spot Price, Annual

# Text Matter for datapackage.json
DATAPACKAGE_JSON = '''{
    "name": "gas-prices",
    "title": "Henry Hub Natural Gas Spot prices listed Daily, Weekly, Monthly and  Annually",
    "resources": [
        {
            "name": "daily_gas_prices",
            "path": "data/daily_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "name": "Price(Dollars per Million Btu)",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "weekly_gas_prices",
            "path": "data/weekly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "name": "Price(Dollars per Million Btu)",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "monthly_gas_prices",
            "path": "data/monthly_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "name": "Price(Dollars per Million Btu)",
                        "type": "float"
                    }
                ]
            }
        },
        {
            "name": "annual_gas_prices",
            "path": "data/annual_gas_prices.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "name": "Price(Dollars per Million Btu)",
                        "type": "float"
                    }
                ]
            }
        }
    ]
}
'''