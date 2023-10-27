# ADM_A3

main.py
    Handles file input output and command line argument parsing and selects 
    which encoder/decoder is used.

binary_encoding.py
    Working version of binary encoder.
    Makes all files bigger which is expected behavior as printing the bytes as
    strings takes more storage.

run_length_encoding.py
    To be implemented

dictionary_encoding.py
    Working version of dictionary encoder.
    Works well on files with few unique values which are long as these get much 
    smaller by using a dictionary (e.g. l_shipdate-string.csv and 
    l_shipinstruct-string.csv). Files with many unique values get bigger after 
    encoding this way.

frame_of_reference_encoding.py  
    To be implemented

differential_encoding.py        
    Working version of differential encoder.
    Works well on files with ascending values (e.g. l_orderkey-int32.csv). This
    is expected and was covered in the lecture. Files where values are randomly
    distributed will benefit less from this encoding, especially when the 
    individual values are small as the negative sign also takes one character 
    (e.g. l_discount-int16.csv).

