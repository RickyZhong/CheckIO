#Your code here
#You can import some modules or create additional functions
from itertools import permutations


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    result = None
    for i in permutations(data):
        for j in range(len(i)):
            if result is None:
                result = abs(sum(i[:j]) - sum(i[j:]))
            else:
                result = min(result, abs(sum(i[:j]) - sum(i[j:])))
    #replace this for solution
    return result

#Some hints
#Your can use combinations if you want use bruteforce


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"