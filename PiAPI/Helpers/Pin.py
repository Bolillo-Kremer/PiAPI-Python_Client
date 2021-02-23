class Pin:

    __in = "in"
    __out = "out"
    __all = "*"
    __high = 1
    __low = 0
    __toggle = -1

    @classmethod
    def in_(cls):
        return cls.__in

    @classmethod
    def out(cls):
        return cls.__out

    @classmethod
    def high(cls):
        return cls.__high

    @classmethod
    def low(cls):
        return cls.__low

    @classmethod
    def toggle(cls):
        return cls.__toggle

    @classmethod
    def all(cls):
        return cls.__all


