class Friends:
    def __init__(self, connections):
        self.__connections = list(connections)

    def add(self, connection):
        return (self.__connections.append(connection) or True) if connection not in self.__connections else False

    def remove(self, connection):
        return (self.__connections.remove(connection) or True) if connection in self.__connections else False

    def names(self):
        return set({y for x in self.__connections for y in x})

    def connected(self, name):
        return set({y for x in self.__connections if name in x for y in x if x != y and y != name})



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"