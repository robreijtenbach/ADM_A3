class BinaryEncoder():
    def encode(self, data, dtype):
        if dtype[:3] != "int":
            raise TypeError
        size = int(dtype[3:])
        encodedData = ""
        for d in data:
            encodedData += f"{int(d):0{size}b}"
        return encodedData

    def decode(self, data, dtype):
        if dtype[:3] != "int":
            raise TypeError
        size = int(dtype[3:])
        decodedData = []
        for i in range(0, len(data), size):
            decodedData.append(int(data[i:i+size], 2))
        return decodedData
