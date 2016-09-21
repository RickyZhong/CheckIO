def check_connection(network, first, second):
    stack = [first]
    used = []
    while stack:
        used.append(stack.pop())
        for item in network:
            tmp_item = item.split("-")
            if tmp_item[0] == used[-1] and tmp_item[1] not in used:
                stack.append(tmp_item[1])
            elif tmp_item[1] == used[-1] and tmp_item[0] not in used:
                stack.append(tmp_item[0])
        if second in stack:
            return True
    else:
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."