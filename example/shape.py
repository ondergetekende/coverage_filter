def squared(value):
    return value + value  # incorrect for demonstration purposes

class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError('invalid dimension')
        self.side = side

    @property
    def area(self):
        return squared(self.side)
