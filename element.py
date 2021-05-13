


class Element:

    def __init__(self, id, name = None):
        self._name = name
        self._id = id


    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self.id
        


