from binary_encoding import BinaryEncoder

class DifferentialEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded bytearray'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        encodedData = [int(data[0])]
        for i in range(1, len(data)):
            difference = int(data[i]) - int(data[i-1])
            encodedData.append(difference)
        binEncoder = BinaryEncoder()
        return binEncoder.encode(data=encodedData, dtype=dtype)

    def decode(self, data, dtype):
        '''Receives data as encoded bytearray as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        if dtype[:3] != "int": 
            raise TypeError
        binEncoder = BinaryEncoder()
        data = binEncoder.decode(data, dtype)
        previousVal = int(data[0])
        decodedData = [previousVal]
        for i in range(1, len(data)):
            currentVal = previousVal + int(data[i])
            decodedData.append(currentVal)
            previousVal = currentVal
        return decodedData
