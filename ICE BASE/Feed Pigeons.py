def checkio(number):
    pigeons = 0
    minutes = 0
    remains = number
    while remains > 0:
        minutes += 1
        pigeons += minutes
        remains -= pigeons

    if remains == 0:
        return pigeons
    elif pigeons + remains <= pigeons - minutes:
        return pigeons - minutes
    else:
        return pigeons + remains

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"