# Henry Hub Natural Gas Spot Prices

This is an exercise in Data Acquisition and Visualization. The dataset used is fetched form the US Energy Information Administration Website

*The prices are listed in Dollars per Million BTU(British Thermal Unit)*

This data repository follows the **Tabular Data Package** format. Read more [here](https://datahub.io/docs/data-packages/tabular)


## To fetch the latest data and generate CSVs

CD into the scripts directory:
```bash
cd scripts
```

Install dependencies from requirements.txt
```bash
pip install -r requirements.txt 
```

Run either of these, one uses the official API, the other scrapes the required data from the `HTML` source:
```python
python gas_prices_api.py
```
### OR
```python
python gas_prices_scrape.py
```

# TODOs

- Add Visualisation
- Add methods to scrape the weekly and annual data from their tables