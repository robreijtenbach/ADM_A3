class RunLengthEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string
        as byte-like object.'''
        encodedData = ""
        if dtype[:3] != "int":
            data = "\n".join(data)
            i = 0
            while i < len(data):
                j = 1
                if data[i].isdigit():
                    encodedData += "*"
                while i+j < len(data) and data[i] == data[i+j]:
                    j += 1
                if j > 1:
                    encodedData += "{}{}".format(data[i], j)
                    i+= j
                else:
                    encodedData += "{}".format(data[i])
                    i+=1
        else:
            i = 0
            len_data = len(data)
            while i < len_data:
                data_i = data[i]
                j = i
                while j < len_data and data_i == data[j]:
                    j += 1
                if j-i > 1:
                    encodedData += "{} {}\n".format(data_i, j-i)
                    i = j
                else:
                    encodedData += "{}\n".format(data_i)
                    i += 1
        return encodedData.encode("utf-8")

    def decode(self, data, dtype):
        '''Receives data as encoded string as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        data = data.decode("utf-8")
        if dtype[:3] != "int":
            decodedData = ""
            i = 0
            while i < len(data):
                if not (data[i].isdigit() or data[i] == "*"):
                    if i+1 < len(data) and data[i+1].isdigit():
                        j = 1
                        occurances = ""
                        while i+j < len(data) and data[i+j].isdigit():
                            occurances += data[i+j]
                            j += 1
                        occurances = int(occurances)
                        for count in range(occurances):
                            decodedData += data[i]
                        i += j-1
                    else:
                        decodedData += data[i]
                #    i += 1
                elif data[i] == "*":
                    i += 1
                    j = 1
                    if i+j < len(data) and data[i+1].isdigit():
                        j = 1
                        occurances = ""
                        while i+j < len(data) and data[i+j].isdigit():
                            occurances += data[i+j]
                            j += 1
                        occurances = int(occurances)
                        for count in range(occurances):
                            decodedData += data[i]
                        i += j-1
                    else:
                        decodedData += data[i]
                i += 1
            return decodedData.split("\n")
        else:
            data = data.split("\n")
            decodedData = []
            for d in data:
                line = d.split(" ")
                if line == ['']:
                    continue
                if len(line) == 2:
                    for i in range(int(line[1])):
                        decodedData.append(line[0])
                else:
                    decodedData.append(line[0])
        return decodedData

