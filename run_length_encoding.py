class RunLengthEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string'''
        # Initialization
        i = 0
        j = 0
        encodedData = ""
        
        for i in range(1, len(data)):
            counter = 1
            char = data[i]
            j = i
            for j in range(1, len(data)):
                if (data[j] == data[j+1]):
                    counter += 1
                    j += 1
                else: break
            encodedData = encodedData + char + "{}\n".format(counter)
            i = j + 1 
        return encodedData
        

    def decode(self, data, dtype):
        '''Receives data as encoded string as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        
        decodedData = []
        i = 0
        
        for i in range(1, len(data)):
            
        return decodedData
