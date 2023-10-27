class DifferentialEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string'''
        # Check if dtype is integer as only these are needed for this encoding
        if dtype[:3] != "int": 
            raise TypeError
        encodedData = "{}\n".format(data[0])
        for i in range(1, len(data)):
            difference = int(data[i]) - int(data[i-1])
            encodedData += "{}\n".format(difference)
        return encodedData

    def decode(self, data, dtype):
        '''Receives data as encoded string as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        if dtype[:3] != "int": 
            raise TypeError
        data = data.split()
        previousVal = int(data[0])
        decodedData = [previousVal]
        for i in range(1, len(data)):
            currentVal = previousVal + int(data[i])
            decodedData.append(currentVal)
            previousVal = currentVal
        return decodedData
