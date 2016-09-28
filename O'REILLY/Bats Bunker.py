from heapq import heapify, heappop, heappush
from collections import namedtuple


def distance(StartPosition, EndPosition):
    x0, y0 = StartPosition
    x1, y1 = EndPosition
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


def canSeeEachOther(walls, StartPosition, EndPosition):
    x0, y0 = StartPosition
    x1, y1 = EndPosition
    dx = x1 - x0
    dy = y1 - y0

    if dx == 0:
        return all([False if (x0, y) in walls else True for y in range(min(y0, y1), max(y0, y1))])
    elif dy == 0:
        return all([False if (x, y0) in walls else True for x in range(min(x0, x1), max(x0, x1))])
    elif abs(dx) >= abs(dy):
        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        k = dy / dx
        start = y0 + k / 2
        for i in range(abs(dx)):
            nowy = start + i * k
            nowx = x0 + i
            if (nowx, int(nowy + 0.5)) in walls or (nowx + 1, int(nowy + 0.5)) in walls:
                return False
            if int(nowy + 0.5) == nowy + 0.5:
                if (nowx, int(nowy + 0.5) - 1) in walls or (nowx + 1, int(nowy + 0.5) - 1) in walls:
                    return False
        return True
    else:
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        k = dx / dy
        start = x0 + k / 2
        for i in range(abs(dy)):
            nowx = start + i * k
            nowy = y0 + i
            if (int(nowx + 0.5), nowy) in walls or (int(nowx + 0.5), nowy + 1) in walls:
                return False
            if int(nowx + 0.5) == nowx + 0.5:
                if (int(nowx + 0.5) - 1, nowy) in walls or (int(nowx + 0.5) - 1, nowy + 1) in walls:
                    return False
        return True



def checkio(bunker):
    bats = [(x, y) for x in range(len(bunker)) for y in range(len(bunker[x])) if bunker[x][y] in ['B', 'A']]
    walls = [(x, y) for x in range(len(bunker)) for y in range(len(bunker[x])) if bunker[x][y] == 'W']
    alpha_bats = [(x, y) for x in range(len(bunker)) for y in range(len(bunker[x])) if bunker[x][y] == 'A']

    Node = namedtuple("Node", ("Priority", "Path"))

    queue = [Node(0, [(0, 0)])]
    heapify(queue)
    visited = set([(0, 0)])

    while queue:
        current = heappop(queue)

        if current.Path[-1] in alpha_bats:
            return current.Priority

        related = [x for x in bats if canSeeEachOther(walls, current.Path[-1], x)]

        for i in related:
            if i in visited:
                continue
            else:
                heappush(queue, Node(current.Priority + distance(current.Path[-1], i), current.Path + [i]))
                visited.add(i)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"