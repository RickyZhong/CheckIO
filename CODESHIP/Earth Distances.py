import re
from math import sin, asin, cos, sqrt, radians


R = 6371


def distance(first, second):
    def parse(x):
        tmp_x = re.split(r'[°′″\']', x)
        tmp = int(tmp_x[0]) + int(tmp_x[1]) / 60 + int(tmp_x[2]) / 60 / 60
        if tmp_x[3] in ['W', 'S']:
            tmp *= -1
        return radians(tmp)

    get_distance = lambda x0, y0, x1, y1: 2 * R * asin(sqrt(sin((x0 - x1) / 2) ** 2 + cos(x0) * cos(x1) * sin((y0 - y1) / 2) ** 2))

    first_latitude, first_longitude = map(parse, [x for x in re.split(r'[ ,(, )]', first) if x])
    second_latitide, second_longitude = map(parse, [x for x in re.split(r'[ ,(, )]', second) if x])

    return get_distance(first_latitude, first_longitude, second_latitide, second_longitude)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"