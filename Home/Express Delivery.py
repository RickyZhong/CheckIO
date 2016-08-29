from collections import namedtuple
from heapq import heappop, heappush, heapify


Node = namedtuple("Node", ("Priority", "Cost", "Position", "Path", "Box"))


def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def get_neighbour(position, maze):
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    neighbours = []

    for direction, (dx, dy) in directions.items():
        x = position[0] + dx
        y = position[1] + dy
        if maze[x][y] != 'W':
            neighbours.append(((x, y), direction))

    return neighbours


def checkio(field_map):
    # Add boundaries
    field_map = ["W" * (len(field_map[0]) + 2)] + \
                ["W" + x+ "W" for x in field_map] + \
                ["W" * (len(field_map[0]) + 2)]

    # Find start goal boxes position
    start = goal = None
    for i in range(len(field_map)):
        for j in range(len(field_map[i])):
            if field_map[i][j] == "S":
                start = (i, j)
            elif field_map[i][j] == "E":
                goal = (i, j)
            elif start and goal:
                break

    # Declare openlist and closelist
    open_list = [Node(0, 0, start, '', True)]
    heapify(open_list)
    closed_list = set()

    # Find solution
    while open_list:
        current = heappop(open_list)
        if current.Position == goal and current.Box:
            return current.Path
        if (current.Position, current.Box) in closed_list:
            continue

        neighbours = get_neighbour(current.Position, field_map)

        # Calculate cost
        cost = 2 if current.Box else 1

        # Unload or Load cargo
        if field_map[current.Position[0]][current.Position[1]] == "B":
            priority = current.Cost + 1 + heuristic(current.Position, goal)
            heappush(open_list,
                     Node(priority, current.Cost + 1, current.Position, current.Path + "B", not current.Box))

        for new_position, direction in neighbours:
            priority = current.Cost + cost + heuristic(new_position, goal)
            heappush(open_list,
                     Node(priority, current.Cost + cost, new_position, current.Path + direction, current.Box))

        closed_list.add((current.Position, current.Box))

    return "N"


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"