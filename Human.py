class Human:
    name: str
    last_name: str
    __id: int
    ids = set()

    def __init__(self, name, last_name, __id=None):
        self.name = name
        self.last_name = last_name
        if __id in self.ids:
            raise Exception("id уже существует")
        elif __id is None:
            if len(self.ids) == 0:
                self.__id = 0
                self.ids.add(self.__id)
            else:
                self.__id = max(self.ids) + 1
                self.ids.add(self.__id)
        else:
            self.__id = __id
            self.ids.add(__id)

    def __lt__(self, other):
        if self.last_name == other.last_name:
            return self.name < other.name
        else:
            return self.last_name < other.last_name

    def __eq__(self, other):
        return self.last_name == other.last_name and self.name == other.name

    def __hash__(self):
        a = "self.name" + " " + "self.last_name"
        return hash(a)
