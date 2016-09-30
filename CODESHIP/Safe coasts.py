def finish_map(regional_map):
    result_map = [[y for y in x.replace('.', 'S')] for x in regional_map]

    change_flag = True
    while change_flag:
        change_flag = False
        for i in range(len(result_map)):
            for j in range(len(result_map[i])):
                if result_map[i][j] == 'S':
                    surronded_area = (result_map[i - 1][max(j - 1, 0): min(j + 2, len(result_map[0]))] if i > 0 else []) + \
                                     (result_map[i][max(j - 1, 0): min(j + 2, len(result_map[0]))]) + \
                                     (result_map[i + 1][max(j - 1, 0): min(j + 2, len(result_map[0]))] if i < len(result_map) - 1 else [])

                    if 'X' not in surronded_area:
                        if (result_map[i - 1][j] == 'D' if i > 0 else False) or \
                                (result_map[i + 1][j] == 'D' if i < len(result_map) - 1 else False) or \
                                (result_map[i][j - 1] == 'D' if j > 0 else False) or \
                                (result_map[i][j + 1] == 'D' if j < len(result_map[0]) - 1 else False):
                            result_map[i][j] = 'D'
                            change_flag = True
                            break
            if change_flag:
                break

    return [''.join(x) for x in result_map]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"