# Importing live data in Hbase
# Hadoop version 3.3.1
# Hbase version 1.4.6
# step 1: start hadoop 
start-all.sh
# step 2: start Hbase
start-hbase.sh
# step 3: run python code
python3 program_name.py
this program fetch live stock data from alpha vantege website using the API key.
After fetching data is stored on hbase table.
Happybase library of python is used in this program to do hbase operations.
