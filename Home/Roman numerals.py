def checkio(data):
    romandict = [
        ["","I","II","III","IV","V","VI","VII","VIII","IX"],
        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["","M","MM","MMM"]
    ]

    result = ""

    result += romandict[3][data // 1000 % 10]
    result += romandict[2][data // 100 % 10]
    result += romandict[1][data // 10 % 10]
    result += romandict[0][data % 10]

    # replace this for solution
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'