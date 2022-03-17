# Henry Hub Natural Gas Spot Prices

This is an exercise in Data Acquisition and Visualization. The dataset used is fetched form the US Energy Information Administration [website](https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm)

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
```bash
python gas_prices_api.py
```
### OR
```bash
python gas_prices_scrape.py
```

## Line Chart Visualization

Navigate to [visualization](https://leabstrait.github.io/gas-prices-data/) for the web version.

***If running locally***

Stay in the project root directory `gas-prices/`:

We could just open up `visualization/index.html` but since some browsers block `CORS` for `file://` protocol it won't display the charts.
In that case: run python's `simple HTTP` server

```bash
python -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```
Then point your browser to `localhost:8000/visualization`. Use any other port if specified while creating the server.

# TODOs

- ~~Add Visualisation~~
- ~~Add methods to scrape the weekly and annual data from their tables~~
