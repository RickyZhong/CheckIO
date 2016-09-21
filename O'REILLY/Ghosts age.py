def checkio(opacity):
    fibs = [1, 1]
    count = 0
    tmp_opacity = 10000
    while tmp_opacity != opacity and count < 5000:
        count += 1
        while count > fibs[-1]:
            fibs.append(fibs[-2] + fibs[-1])
        tmp_opacity += (1, -count)[count in fibs]
    else:
        return (count, 0)[opacity == 10000]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"