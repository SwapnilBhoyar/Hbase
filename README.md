# Store output of word count in Hbase
# Hadoop version 3.3.1
# Hbase version 1.4.6
# step 1: start hadoop 
start-all.sh
# step 2: start Hbase
start-hbase.sh
# step 3: run python code
python3 program_name.py
this program use file which contains the word count program output.
Happybase library of python is used in this program to do hbase operations.
