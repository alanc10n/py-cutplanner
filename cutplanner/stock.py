class Stock(object):
    """ Defines a piece of stock, including planned cuts """

    def __init__(self, length):
        self.pieces = []
        self.length = length
        self.remaining_length = length

    @property
    def used_length(self):
        return self.length - self.remaining_length

    def cut(self, piece, loss=0.0):
        """ Cut given amount from this stock """
        if (loss + piece.length) > self.remaining_length:
            raise ValueError("Stock too small to cut piece")

        self.pieces.append(piece)
        self.remaining_length -= (loss + piece.length)
        return self.remaining_length

    def shrink(self, new_length):
        """ Attempt to reduce stock size, to minimize waste when possible. """
        if new_length < self.used_length:
            return None

        self.remaining_length = new_length - self.used_length
        self.length = new_length
        return new_length
