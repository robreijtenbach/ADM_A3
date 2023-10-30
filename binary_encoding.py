class BinaryEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, bytearray.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        size = int(int(dtype[3:])/8) # Size in bytes
        encodedData = bytearray()
        for d in data:
            encodedData += bytearray(int(d).to_bytes(size, byteorder='big', signed=True))
        return encodedData

    def decode(self, data, dtype):
        '''Receives data as encoded bytearray as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int":
            raise TypeError
        size = int(int(dtype[3:])/8) # Size in bytes
        print(data[0:2])
        decodedData = []
        for i in range(0, len(data), size):
            decodedData.append(int.from_bytes(data[i:i+size], byteorder='big', signed=True))
        return decodedData
