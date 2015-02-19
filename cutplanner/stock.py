class Stock(object):
    """ Defines a piece of stock, including planned cuts """

    def __init__(self, length):
        self.pieces = []
        self.length = length
        self.remaining_length = length


