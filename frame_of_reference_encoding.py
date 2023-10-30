class FrameOfReferenceEncoder():
    '''Does not use binary encoding as it is hard to encode which values are 
     differences and which values are references.'''
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string as
        byte-like object.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        # Experimentially found to be good value for max difference.
        # Base 10 as this file uses utf-8 encding for encoded file.
        MAX_DIFFERENCE = 999 
        reference = int(data[0])

        encodedData = "N{}\n".format(reference)
        for i in range(1, len(data)):
            difference = int(data[i]) - int(reference)
            if abs(difference) > MAX_DIFFERENCE:
                reference = data[i]
                encodedData += "N{}\n".format(reference)
            else:
                encodedData += "{}\n".format(difference)
        return encodedData.encode("utf-8")

    def decode(self, data, dtype):
        '''Receives data as encoded bytearray as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        data = data.decode("utf-8").split()

        decodedData = []
        for d in data:
            if d[0] == 'N':
                reference = int(d[1:])
                decodedData.append(reference)
            else:
                decodedData.append(reference + int(d))
        return decodedData

