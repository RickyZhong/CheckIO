def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    tmp_pyramid = [list(x) for x in pyramid]

    for level in range(1, len(tmp_pyramid)):
        for item in range(len(tmp_pyramid[level])):
            if item == 0:
                tmp_pyramid[level][item] += tmp_pyramid[level - 1][item]
            elif item == len(tmp_pyramid[level]) - 1:
                tmp_pyramid[level][item] += tmp_pyramid[level - 1][item - 1]
            else:
                tmp_pyramid[level][item] += max(tmp_pyramid[level - 1][item], tmp_pyramid[level - 1][item - 1])

    #replace this for solution
    return max(tmp_pyramid[-1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

