from heapq import heapify, heappush, heappop
from collections import namedtuple


def get_options(position, puzzle):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    options = []

    for direction, (dx, dy) in directions.items():
        x = position[0] + dx
        y = position[1] + dy
        if 0 <= x < len(puzzle) and 0 <= y < len(puzzle[0]):
            options.append(((x, y), direction))

    return options


def checkio(puzzle):
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """

    column = len(puzzle)
    row = len(puzzle[0])

    Node = namedtuple("Node", ('Priority', 'Path', 'Position', 'Puzzle'))

    start = [(x, y) for x in range(column) for y in range(row) if puzzle[x][y] == 0]
    goal = [[(0, y + 1)[y + 1 < row * column] for y in range(row * x, row * x + row)] for x in range(column)]
    queue = [Node(0, "", start[0], puzzle)]
    heapify(queue)
    visited = set()

    while queue:
        current = heappop(queue)
        if current.Puzzle == goal:
            print(current.Path)
            return current.Path
        if hash(str(current.Puzzle)) in visited:
            continue
        options = get_options(current.Position, current.Puzzle)
        for new_position, direction in options:
            tmp_puzzle = [x[:] for x in current.Puzzle]
            tmp_puzzle[new_position[0]][new_position[1]], tmp_puzzle[current.Position[0]][current.Position[1]] = \
                tmp_puzzle[current.Position[0]][current.Position[1]], tmp_puzzle[new_position[0]][new_position[1]]
            if hash(str(tmp_puzzle)) in visited:
                continue
            heappush(queue, Node(current.Priority + 1, current.Path + direction, new_position, tmp_puzzle))
        visited.add(hash(str(current.Puzzle)))


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"