#!/bin/bash

# Initiate python env
python3 -m venv env
source env/bin/activate
pip3 install dask pyarrow pandas


# Download CSV dataset
wget https://zenodo.org/records/5199540/files/ALLFLOWMETER_HIKARI2021.csv.zip
unzip ALLFLOWMETER_HIKARI2021.csv.zip
mv ALLFLOWMETER_HIKARI2021.csv hikari.csv
rm ALLFLOWMETER_HIKARI2021.csv.zip

wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
