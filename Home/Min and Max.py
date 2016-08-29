def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    tmp_min = None
    tmp_result = None

    if len(args) == 1 and type(args[0]) not in [int, float]:
        args = args[0]

    for i in args:
        if tmp_min == None:
            tmp_min = i
            tmp_result = key(i)
        if key(i) < tmp_result:
            tmp_min = i
            tmp_result = key(i)
    return tmp_min


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    tmp_max = None
    tmp_result = None

    if len(args) == 1 and type(args[0]) not in [int, float]:
        args = args[0]

    for i in args:
        if tmp_max == None:
            tmp_max = i
            tmp_result = key(i)
        if key(i) > tmp_result:
            tmp_max = i
            tmp_result = key(i)
    return tmp_max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"