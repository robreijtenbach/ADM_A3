# ADM_A3

main.py
    Handles file input output and command line argument parsing and selects 
    which encoder/decoder is used.

binary_encoding.py
    Working version of binary encoder.
    Should not make files bigger anymore as it first checks if larger bit 
    formats are actually needed. If not uses less bits.

run_length_encoding.py
    Working version of run length encoder.
    Reduces size of files with many the same values. Very slow on large string
    files. l_comment-strings.csv takes more than a minute to encode or decode.

dictionary_encoding.py
    Working version of dictionary encoder.
    Works well on files with few unique values which are long as these get much 
    smaller by using a dictionary (e.g. l_shipdate-string.csv and 
    l_shipinstruct-string.csv). 

frame_of_reference_encoding.py  
    Working version of frame of reference encoder.
    Works well on files with values that are not too different close together.
    (e.g. l_orderkey-int32.scv). Does not use binary encoder as it is hard to 
    differentiate between reference values and difference values that way.
    Prefixes new reference values with 'N' character.

differential_encoding.py
    Working version of differential encoder.
    Works well on files with ascending values (e.g. l_orderkey-int32.csv). This
    is expected and was covered in the lecture. Files where values are randomly
    distributed will benefit less from this encoding, especially when the 
    individual values are small as the negative sign also takes one character 
    (e.g. l_discount-int16.csv). Uses binary encoding aswell now.

