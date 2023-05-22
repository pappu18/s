
from collections import deque

def bfs(x, y, target):
    queue = deque([(0, 0, [])])  # (x, y, path)
    visited = set()
    while queue:
        curr_x, curr_y, path = queue.popleft()
        if curr_x == target and curr_y == 0 or (curr_x == 0 and curr_y == target):
            return path + [(curr_x, curr_y)]

        if (curr_x, curr_y) in visited:
            continue

        visited.add((curr_x, curr_y))

        operations = [
            ('Fill X', x, curr_y),
            ('Fill Y', curr_x, y),
            ('Empty X', 0, curr_y),
            ('Empty Y', curr_x, 0),
            ('Pour X to Y', max(0, curr_x + curr_y - y), min(y, curr_x + curr_y)),
            ('Pour Y to X', min(x, curr_x + curr_y), max(0, curr_x + curr_y - x))
        ]

        for operation, next_x, next_y in operations:
            queue.append((next_x, next_y, path + [(curr_x, curr_y, operation)]))

    return None

j1 = int(input("Enter the quantity of jug 1: "))
j2 = int(input("Enter the quantity of jug 2: "))
target = int(input("Enter the target amount: "))

solution = bfs(j1, j2, target)

if solution:
    print("BFS solution:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
