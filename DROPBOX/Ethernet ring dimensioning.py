from math import ceil


ETHERNET = (100, 40, 10, 1, 0.1) # Ethernet bandwidth capacity in Gbps


def checkio(ring, *flows):
    clockwise = lambda x, y: ring[x: y + 1] if y >= x else ring[x:] + ring[:y+1]
    anticlockwise = lambda x, y: ring[x::-1] + ring[-1:y - len(ring) - 1:-1] if y >= x else ring[y:x+1][::-1]
    result = {}

    for flow in flows:
        s, dr = flow

        x, y = [ring.index(x) for x in s]
        shortestPath = min(clockwise(x, y), anticlockwise(x, y), key=len)

        for i in range(len(shortestPath) - 1):
            if ''.join(shortestPath[i:i+2]) in shortestPath:
                try:
                    result[''.join(sorted(shortestPath[i:i+2]))] += dr
                except Exception:
                    result[''.join(sorted(shortestPath[i:i+2]))] = dr

    result_list = [0, 0, 0, 0, 0]
    for k, v in result.items():
        isMatched = False
        for i in range(len(ETHERNET)):
            if v >= 100:
                isMatched = True
                result_list[i] += ceil(v / 100)
                break
            if v > ETHERNET[i]:
                isMatched = True
                result_list[i - 1] += 1
                break
        else:
            if not isMatched:
                result_list[-1] += 1

    return result_list


if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]