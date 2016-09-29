def checkio(data):
    #replace this for solution
    parse = [''.join(['{:0>8b}'.format(int(y)) for y in x.split(".")]) for x in data]
    result = ''
    length = 0
    for i in range(32):
        tmp = None
        is_same = True
        for j in parse:
            if tmp is None:
                tmp = j[i]
            if tmp != j[i]:
                is_same = False
                break

        if is_same:
            result += tmp
        else:
            length = i
            result = "{:0<32}".format(result)
            break

    return "{}/{}".format(".".join([str(int(result[x * 8: x * 8 + 8], 2)) for x in range(4)]), length)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"