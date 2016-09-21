# Your code here
# You can import some modules or create additional functions
import re

def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.
    pattern = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10}"
    o = re.compile(pattern)
    # replace this for solution
    return True if o.search(data) else False


# Some hints
# Just check all conditions


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"