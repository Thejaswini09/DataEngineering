"""
Please complete the following tasks:
    # 1. Outfit the below class with the code for __init__
    # 2. In the init method, read the specified file
    # 3. Arange the data in a way such that it can be easily iterated over 
    # (can be done in conjunction with 2!)
    # 4. Add functionality such that single items can be referecend 
    # directly ([i])
    5. (optional) write the data to a binary file, 
    value by value and add a small parser class
"""

import pickle
import numpy as np

class DataHandler:

    def __init__(self, filename, binname):
        self.filename = filename
        self.binname = binname
        self.data = []
        self.read_file()

    def read_file(self):
        '''
        Reading and parsing the file
        '''
        with open(self.filename, 'r') as file:
            # Accessing and Processing lines
            lines = [line.strip().split(';') for line in file]
            # Mapping of string values to float (in case)
            self.data = [list(map(float, line)) for line in lines]

    def write2bin(self):
        '''
        Loading data into binary file
        '''
        with open(self.binname, 'wb') as bin_file:
            pickle.dump(self.data, bin_file)

class BinParser:

    def __init__(self, filename):
        self.binfile = filename
        self.data = []
        self.read_bin_file()

    def read_bin_file(self):
        '''
        Reading data from binary file
        '''
        with open(self.binfile, 'rb') as bin_file:
            self.data = pickle.load(bin_file)
    
    def __getitem__(self, index):
        '''
        Accessing items
        '''
        return self.data[index]


if __name__ == "__main__":

    # File paths
    FNAME = 'datfile.txt'
    FNAME_BIN = 'binfile'

    # Initiating DataHandler class
    handler = DataHandler(FNAME, FNAME_BIN)
    handler.write2bin()  

    # Initiating BinParser class
    parser = BinParser(FNAME_BIN)

    # Accessing the first item in the binary file
    print(parser[0])  
    # Accessing the first element from the first item
    print(parser[0][0])
