class Edge:
    __rising = "rising"
    __falling = "falling"
    __both = "both"

    @classmethod
    def rising(cls):
        return cls.__rising

    @classmethod
    def falling(cls):
        return cls.__falling

    @classmethod
    def both(cls):
        return cls.__both