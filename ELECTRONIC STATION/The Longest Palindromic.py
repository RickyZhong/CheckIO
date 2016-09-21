def longest_palindromic(text):
    for length in reversed(range(1, len(text) + 1)):
        for start in range(len(text) - length + 1):
            subtext = text[start:start + length]
            if subtext == subtext[::-1]:
                return subtext

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"