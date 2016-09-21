from functools import namedtuple

Node = namedtuple("Node", ("Priority", "Path"))


def checkio(teleports_string):
    # return any route from 1 to 1 over all points
    # Don't remove checkio function
    teleports = teleports_string.split(",")
    queue = [Node(0, "1")]

    while queue:
        current = queue.pop()

        if all([(False, True)[str(x) in current.Path] for x in range(1, 9)]) and current.Path[-1] == '1':
            return current.Path

        related = [x for x in teleports if current.Path[-1] in x]
        visited = ["".join((i[::-1], i)["".join(i) in teleports]) for i in zip(current.Path, current.Path[1:])]

        for i in related:
            if i in visited:
                continue
            else:
                queue.append(Node(current.Priority + 1, current.Path + (i[0], i[1])[i[0] == current.Path[-1]]))
    else:
        return "N"


if __name__ == "__main__":
    print(checkio("12,23,34,45,56,67,78,81"))  # "123456781"
    print(checkio("12,28,87,71,13,14,34,35,45,46,63,65"))  # "1365417821"
    print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56"))  # "12382478561"
    print(checkio("13,14,23,25,34,35,47,56,58,76,68"))  # "132586741"