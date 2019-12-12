import csv
from os import mkdir
from os.path import join, exists

import constants

# Make the data dir if doesn't exist
def make_data_dir():
    if not exists(constants.DATA_DIR):
        mkdir(constants.DATA_DIR)

# Write data to the provided CSV fle
def toCSV(dataRows, csvFile):
    header = ['date', 'price']
    with open(csvFile, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(dataRows)

# Write the datapackage.json file
def makeDatapackage():
    f = open('../datapackage.json', 'w+')
    f.write(constants.DATAPACKAGE_JSON)
    f.close()