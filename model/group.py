

class Group:

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return self.name == other.name