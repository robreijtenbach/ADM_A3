#!/bin/python3

import csv
import sys
import time
import os

from numpy import mean

from binary_encoding import BinaryEncoder
from run_length_encoding import RunLengthEncoder
from dictionary_encoding import DictionaryEncoder
from frame_of_reference_encoding import FrameOfReferenceEncoder
from differential_encoding import DifferentialEncoder

from main import readInput, writeBytes, readBytes, printLikeInput

NUM_RUNS = 1

def writeLikeInput(filename, data):
    with open(filename, "w") as f:
        for d in data:
            f.write(str(d)+"\n")

def main():
    if len(sys.argv) != 2:
        print("Usage {sys.argv[1]} \{path to files to be encoded\}")
        exit(1)

    path = sys.argv[1]
    filenames = sorted(os.listdir(path))
    if "tmp" in filenames:
        filenames.remove("tmp")
    datatypes = ["int8", "int16", "int32", "int64", "string"]
    methods = ["bin", "rle", "dic", "dif", "for"]

    for f in filenames:
        if f[-4:] != ".csv":
            print(f"Incorrect file found in folder {path}: {f}.")
            exit(1)

    counter = 0
    print('''\\begin{table}[]
\\centering
\\resizebox{\\textwidth}{!}{\\begin{tabular}{c||cccccc}
& Original & \\begin{tabular}[c]{@{}c@{}}Binary\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Run length\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Dictionary\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Differential\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Frame of reference\\\\ encoding\\end{tabular} \\\\
\\hline''' )

    for f in filenames:
        read_times = []
        write_times = []
        encode_times = [0]
        decode_times = [0]
        file_sizes = []
        compression_rates = [1]
        
        original_size = os.path.getsize(path+f)

        file_sizes.append(original_size/1000000)

        # Read original file time
        start_time = time.time()
        data = readInput(path+f)
        read_times.append(time.time() -start_time)

        # Write original file to tmp folder to check write times
        start_time = time.time()
        writeLikeInput(path+"tmp/"+f, data) 
        write_times.append(time.time()-start_time)

        for method in methods:
            # Select encoder
            if method == 'bin':
                encoder = BinaryEncoder()
            elif method == 'rle':
                encoder = RunLengthEncoder()
            elif method == 'dic':
                encoder = DictionaryEncoder()
            elif method == 'for':
                encoder = FrameOfReferenceEncoder()
            elif method == 'dif':
                encoder = DifferentialEncoder()
            else:
                raise Exception("Error selecting encoder.")

            # Select datatype
            for dt in datatypes:
                if dt in f:
                    datatype = dt
                    break

            if datatype == "string" and (method == "bin" or method == "for" or method == "dif"):
                encode_times.append(0)
                decode_times.append(0)
                write_times.append(0)
                read_times.append(0)
                file_sizes.append(0)
                compression_rates.append(0)
                decoded_data = data
                continue

            # Time encoding
            start_time = time.time()
            encoded_data = encoder.encode(data, datatype)
            encode_times.append(time.time()-start_time)

            # Time write encoded data
            start_time = time.time()
            writeBytes("{}.{}".format(path+"tmp/"+f, method), encoded_data)
            write_times.append(time.time()-start_time)
            
            # Time read encoded data
            start_time = time.time()
            encoded_data = readBytes("{}.{}".format(path+"tmp/"+f, method))
            read_times.append(time.time()-start_time)

            # Time decoding
            start_time = time.time()
            decoded_data = encoder.decode(encoded_data, datatype)
            decode_times.append(time.time()-start_time)

            # Write decoded data for checking
            writeLikeInput("{}.{}.{}".format(path+f, method, "csv"), decoded_data)
            
            encoded_size = os.path.getsize("{}.{}".format(path+"tmp/"+f, method))
            compression_rates.append(encoded_size/original_size)
            file_sizes.append(encoded_size/1000000)

        def printList(l):
            rs = ""
            for el in l:
                if el == 0:
                    rs += ''' & n/a'''
                else :
                    rs += (" & {:.3f}".format(el))
            return rs

        def printList2(l):
            rs = ""
            for el in l:
                if el == 0:
                    rs += ''' & n/a'''
                else :
                    rs += (" & {:.0f}".format(el))
            return rs


        print('''\\hline''')
        print(f"l\\_{f[2:]} &  &  &  &  &  &  \\\\")
        print(f"Read time (s) {printList(read_times)}  \\\\")
        print(f"Write time (s) {printList(write_times)}  \\\\")
        print(f"Encode time (s) {printList(encode_times)}  \\\\")
        print(f"Decode time (s) {printList(decode_times)}  \\\\")
        print(f"File size (MB){printList2(file_sizes)}  \\\\")
        print(f"Compression rate {printList(compression_rates)}  \\\\")

        counter += 1

        if counter == 6:
            counter = 0
            print('''\\end{tabular}}
\\end{table}''')
            print('''\\begin{table}[]
\\centering
\\resizebox{\\textwidth}{!}{\\begin{tabular}{c||cccccc}
& Original & \\begin{tabular}[c]{@{}c@{}}Binary\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Run length\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Dictionary\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Differential\\\\ encoding\\end{tabular} & \\begin{tabular}[c]{@{}c@{}}Frame of reference\\\\ encoding\\end{tabular} \\\\
\\hline''' )


    print('''\\end{tabular}}
\\end{table}''')






#    # Read data, encode or decode and print accordingly
#    if config['direction'] == 'en':
#        data = readInput(config['path'])
#        start_time = time.time()
#        data = encoder.encode(data, config['datatype'])
#        print("Encoding {} took {:.3f} seconds using the {} algorithm".format(config['path'], time.time()-start_time, config['method']), file=sys.stderr)
#        writeBytes("{}.{}".format(config['path'],config['method']), data)
#    elif config['direction'] == 'de':
#        data = readBytes(config['path'])
#        start_time = time.time()
#        data = encoder.decode(data, config['datatype'])
#        print("Decoding {} took {:.3f} seconds using the {} algorithm".format(config['path'], time.time()-start_time, config['method']), file=sys.stderr)
#        printLikeInput(data)
#    else:
#        raise Exception("Error selecting encode or decode.")

if __name__ == "__main__":
    main()

