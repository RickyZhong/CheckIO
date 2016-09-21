def checkio(marbles, step):
    heap = [[marbles, 1]]
    parse = lambda x: 'w' if x == 'b' else 'b'
    for i in range(step - 1):
        for _ in range(2 ** i):
            parent_index = (len(heap) - 1) // 2
            parent_marbles = heap[parent_index][0]
            parent_value = heap[parent_index][1]

            if 'w' in parent_marbles:
                tmp_w_marbles = parent_marbles[:parent_marbles.index("w")] + \
                              parse(parent_marbles[parent_marbles.index("w")]) + \
                              parent_marbles[parent_marbles.index("w") + 1:]
                tmp_w_value = parent_marbles.count("w") * parent_value
            else:
                tmp_w_marbles = ""
                tmp_w_value = 0

            if 'b' in parent_marbles:
                tmp_b_marbles = parent_marbles[:parent_marbles.index("b")] + \
                                parse(parent_marbles[parent_marbles.index("b")]) + \
                                parent_marbles[parent_marbles.index("b") + 1:]
                tmp_b_value = parent_marbles.count("b") * parent_value
            else:
                tmp_b_marbles = ""
                tmp_b_value = 0

            heap.append([tmp_w_marbles, tmp_w_value])
            heap.append([tmp_b_marbles, tmp_b_value])

    count = sum([x[1] * x[0].count('w') for x in heap[(len(heap) - 1) // 2:]])

    return float("{:.2f}".format(count / len(marbles) ** step))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"