class DifferentialEncoder():
    def encode(self, data, dtype):
        '''Receives data as list of input items, returns encoded data string'''
        raise NotImplementedError

    def decode(self, data, dtype):
        '''Receives data as encoded string as created by encode function. 
        Returns list of items that are the same as input of encode function.'''
        raise NotImplementedError
