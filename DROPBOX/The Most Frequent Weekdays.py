from calendar import Calendar, day_name


def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    calendar = Calendar(firstweekday=0)
    i = calendar.yeardatescalendar(year, 1)
    result = [x.isoweekday() for x in i[0][0][0] + i[-1][-1][-1] if x.year == year]
    return [day_name[x - 1] for x in set(result) if result.count(x) == result.count(max(result, key=result.count))]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"