"""
@Author: Swapnil Bhoyar
@Date: 2021-08-11
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-11
@Title : This program create hbase table from csv file.
"""

from os import write
import happybase as hb
from Log import logger
import csv


def connect():
    """
    Description:
        This function is used for creating connection with hbase
     Return:
        It return a conn 
    """
    try:
        conn = hb.Connection()
        conn.open()
        return conn
    except Exception as e:
        logger.error(e)

def creating_table():
    """
    Description:
        This function is used for creating hbase table
    """
    try:
        connection = connect()
        connection.create_table('wordcount',{'cf1': dict(),'cf2': dict()})
        logger.info("table created successfully")
       
    except Exception as e: 
        logger.error(e)
        connection.close()

def write_data():
    """
    Description:
        This function is used for putting csv data into hbase table
    """
    try:
        connection = connect()
        table = connection.table('wordcount')
        input_file = csv.DictReader(open("input"))
        for row in input_file:
            table.put(row['id'],
        {'cf1:String': row['string'],
         'cf2:Count': row['count']})       
    except Exception as e: 
        logger.error(e)
        connection.close()
        
def display_data():
    """
    Description:
        This function is used for displaying data from hbase table.
    """
    try:
        connection = connect()
        table = connection.table('wordcount')
        for key,data in table.scan():
            id = key.decode('utf-8')
            for value1,value2 in data.items():
                cf1 = value1.decode('utf-8')
                cf2 = value2.decode('utf-8')
                print(id,cf1,cf2) 

    except Exception as e:
        logger.error(e)

creating_table()
write_data()
display_data()