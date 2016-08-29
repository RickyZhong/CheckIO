def checkio(game_result):
    tmp_result = [list(line) for line in game_result]

    for x, y, z in tmp_result:
        if x == y == z and x != ".":
            return x

    if tmp_result[0][0] == tmp_result[1][1] == tmp_result[2][2] and tmp_result[0][0] != ".":
        return tmp_result[0][0]

    if tmp_result[0][2] == tmp_result[1][1] == tmp_result[2][0] and tmp_result[0][2] != ".":
        return tmp_result[0][2]

    for x, y, z in zip(*tmp_result):
        if x == y == z and x != ".":
            return x

    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"