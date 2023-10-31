#!/bin/python3

import csv
import sys
import time

from binary_encoding import BinaryEncoder
from run_length_encoding import RunLengthEncoder
from dictionary_encoding import DictionaryEncoder
from frame_of_reference_encoding import FrameOfReferenceEncoder
from differential_encoding import DifferentialEncoder

def invalidInput():
    '''Prints usage if program is called incorrectly and exits.'''
    print(f"Usage: {sys.argv[0]} " + '''{en|de} {bin|rle|dic|for|dif} 
    {int8|int16|int32|int64|string} {path}.csv (for decoding filename can not 
    end in .csv to avoid confusion during testing).''', file=sys.stderr)
    exit(-1)

def readInput(filename):
    '''Used for reading input csv files. Returns list of input lines'''
    data = []
    with open(filename, 'r') as f:
        for row in csv.reader(f, delimiter = '\n'):
            if len(row) == 1:
                data.append(row[0])
            else:
                data.append(row) 
    return data

def readBytes(filename):
    '''Function to read encoded binary files'''
    with open(filename, 'rb') as f:
        data = bytearray()
        while (byte := f.read(1)):
            data += byte
    return data

def printLikeInput(data):
    '''Prints data like input file line by line to stdout. Used to compare to 
    original after decoding.'''
    for item in data:
        print(item)

def writeBytes(filename, data):
    '''Function to write encoded binary files. Needs byte-like object data.'''
    with open(filename, 'wb') as f:
        f.write(data)

def main():
    # Check if program is called correctly
    if len(sys.argv) != 5:
        print("len(argv) not correct.", file=sys.stderr)
        invalidInput()
    if not (sys.argv[1] == "en" or sys.argv[1] == "de"):
        print("Not encode or decode.", file=sys.stderr)
        invalidInput()
    if not (sys.argv[2] == "bin" or sys.argv[2] == "rle" or sys.argv[2] == "dic" or sys.argv[2] == "for" or sys.argv[2] == "dif"):
        print("No correct algorithm", file=sys.stderr)
        invalidInput()
    if not (sys.argv[3] == "int8" or sys.argv[3] == "int16" or sys.argv[3] == "int32" or sys.argv[3] == "int64" or sys.argv[3] == "string"):
        print("No correct datatype.", file=sys.stderr)
        invalidInput()
    if not sys.argv[4][-4:] == ".csv" and sys.argv[1] == "en":
        print("No .csv for file to be encoded.", file=sys.stderr)
        invalidInput()
    if not sys.argv[4][-3:] == sys.argv[2] and sys.argv[1] == "de":
        print('''Encoded file supplied does not have the file extension of the decoder argument passed.''', file=sys.stderr)
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
        start_time = time.time()
        data = encoder.encode(data, config['datatype'])
        print("Encoding {} took {:.3f} seconds using the {} algorithm".format(config['path'], time.time()-start_time, config['method']), file=sys.stderr)
        writeBytes("{}.{}".format(config['path'],config['method']), data)
    elif config['direction'] == 'de':
        data = readBytes(config['path'])
        start_time = time.time()
        data = encoder.decode(data, config['datatype'])
        print("Decoding {} took {:.3f} seconds using the {} algorithm".format(config['path'], time.time()-start_time, config['method']), file=sys.stderr)
        printLikeInput(data)
    else:
        raise Exception("Error selecting encode or decode.")

if __name__ == "__main__":
    main()

