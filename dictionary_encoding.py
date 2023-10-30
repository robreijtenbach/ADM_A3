import ast

class DictionaryEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string
        as byte-like object.'''
        # Initialization
        i = 0
        dictionary = {}
        encodedData = ""

        # Creates dictionary and encoded data.
        for d in data:
            if d not in dictionary.keys():
                dictionary[d] = i
                i += 1
            encodedData += "{}\n".format(dictionary[d])
        
        # Adds the dictionary to the encoded data.
        encodedData = "{}\n{}".format(str(dictionary), encodedData)
        return encodedData.encode("utf-8")

    def decode(self, data, dtype):
        '''Receives data as encoded string as byte-like object as created by 
        encode function. Returns list of items that are the same as input of 
        encode function.'''
        data = data.decode("utf-8").split("\n")
        # Get dictionary from encoded file.
        dictionary = ast.literal_eval(data[0])
        
        # Flips keys and values for more efficient decoding.
        # Works because all values are unique.
        decodeDict = dict([(val, key) for key, val in dictionary.items()]) 

        # Decodes the data.
        decodedData = []
        for d in data[1:-1]:
            decodedData.append(decodeDict[int(d)])
        return decodedData
