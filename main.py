#!/bin/python3

import csv
import sys

from binary_encoding import BinaryEncoder
from run_length_encoding import RunLengthEncoder
from dictionary_encoding import DictionaryEncoder
from frame_of_reference_encoding import FrameOfReferenceEncoder
from differential_encoding import DifferentialEncoder

def invalidInput():
    '''Prints usage if program is called incorrectly and exits.'''
    print("Usage: {sys.argv[0]} \{en|de\} \{bin|rle|dic|for|dif\} \{int8|int16|int32|int64|string\} \{path\}")
    exit(-1)

def readInput(filename):
    '''Used for reading input csv files. Returns list of input lines'''
    data = []
    with open(filename, 'r') as f:
        for row in csv.reader(f, delimiter = '\n'):
            if len(row) == 1:
                data.append(row[0])
            else: # Not certain if this ever happend if not: remove these lines (should test with string input files)
                data.append(row) 
    return data

def readRaw(filename):
    '''Used for reading encoded files.'''
    with open(filename, 'r') as f:
        data = f.read()
    return data

def printLikeInput(data):
    '''Prints data like input file line by line. Used to compare to original 
    after decoding.'''
    for item in data:
        print(item)

def writeData(filename, data):
    '''Function to write encoded file.'''
    with open(filename, 'w') as f:
        f.write(data)

def printRaw(data):
    '''Simple print function to print encoded data to stdout. Used for 
    debugging'''
    print(data, end="")

def main():
    # Check if program is called correctly
    if len(sys.argv) != 5:
        invalidInput()
    if not (sys.argv[1] == "en" or sys.argv[1] == "de"):
        invalidInput()
    if not (sys.argv[2] == "bin" or sys.argv[2] == "rle" or sys.argv[2] == "dic" or sys.argv[2] == "for" or sys.argv[2] == "dif"):
        invalidInput()
    if not (sys.argv[3] == "int8" or sys.argv[3] == "int16" or sys.argv[3] == "int32" or sys.argv[3] == "int64" or sys.argv[3] == "string"):
        invalidInput()

    # Generate config dictionary from command line arguments
    config = {
        'direction': sys.argv[1],
        'method': sys.argv[2],
        'datatype': sys.argv[3],
        'path': sys.argv[4]
    }
    
    # Select encoder
    if config['method'] == 'bin':
        encoder = BinaryEncoder()
    elif config['method'] == 'rle':
        encoder = RunLengthEncoder()
    elif config['method'] == 'dic':
        encoder = DictionaryEncoder()
    elif config['method'] == 'for':
        encoder = FrameOfReferenceEncoder()
    elif config['method'] == 'dif':
        encoder = DifferentialEncoder()
    else:
        raise Exception("Error selecting encoder.")

    # Read data, encode or decode and print accordingly
    if config['direction'] == 'en':
        data = readInput(config['path'])
        data = encoder.encode(data, config['datatype'])
        writeData("{}.{}".format(config['path'],config['method']), data)
        #printRaw(data) # Just for debugging
    elif config['direction'] == 'de':
        data = readRaw(config['path'])
        data = encoder.decode(data, config['datatype'])
        printLikeInput(data)
    else:
        raise Exception("Error selecting encode or decode.")

if __name__ == "__main__":
    main()

