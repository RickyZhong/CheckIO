def letter_queue(commands):
    queue = []
    commands = [x.split() for x in commands]
    for i in commands:
        if i[0] == 'PUSH':
            queue.append(i[1])
        elif i[0] == 'POP' and queue:
            queue.pop(0)
    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"