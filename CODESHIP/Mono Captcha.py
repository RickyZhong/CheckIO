FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def split_image(image):
    result = [[] for _ in range((len(image[0]) - 1) // 4)]
    for i in range(len(image)):
        for j in range((len(image[i]) - 1) // 4):
            result[j].append(image[i][j * 4: j * 4 + 5])
    return result


def find_different(image1, image2):
    count = 0
    for y in range(len(image1)):
        for x in range(len(image1[y])):
            if image1[y][x] != image2[y][x]:
                count += 1
            if count > 1:
                break

    return (True, False)[count > 1]


def checkio(image):
    font = [(0, 1)[x == 'X'] for x in FONT]
    font = [font[x * 41: x * 41 + 41] for x in range(len(FONT) // 41)]

    font_split = split_image(font)
    image_split = split_image(image)

    result = 0
    for i in image_split:
        for j in range(len(font_split)):
            if find_different(i, font_split[j]):
                result = result * 10 if j == 9 else result * 10 + j + 1

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"