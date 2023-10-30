class BinaryEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns bytearray.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        size = int(int(dtype[3:])/8) # Size in bytes

        data = [int(d) for d in data]
        maxAbsVal = max(max(data),-min(data))
        
        # Check if size could be smaller
        if maxAbsVal < 2**7:
            size = 1
        elif maxAbsVal < 2**15:
            size = 2
        elif maxAbsVal < 2**31:
            size = 4
        elif maxAbsVal < 2**63:
            size = 8

        encodedData = bytearray()
        encodedData += size.to_bytes(1, byteorder='big') #first byte of file is size
        for d in data:
            encodedData += int(d).to_bytes(size, byteorder='big', signed=True)
        return encodedData

    def decode(self, data, dtype):
        '''Receives data as encoded bytearray as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int":
            raise TypeError

        # First byte of file is size
        size = int.from_bytes(data[0:1], byteorder='big', signed=True) 
        decodedData = []
        for i in range(1, len(data), size):
            decodedData.append(int.from_bytes(data[i:i+size], byteorder='big', signed=True))
        return decodedData
