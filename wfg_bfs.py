'''from collections import deque
j1=int(input("Enter j1 capacity:"))
j2=int(input("Enter j2 capacity:"))
def bfs(start, goal):
    queue = deque([(start, [])])
    while queue:
        node, path = queue.popleft()
        x, y = node
        if node == goal:
            return path
        if x < j1:
            queue.append(((j1, y), path + [('fill x', j1, y)]) )
        if y < j2:
            queue.append(((x, j2), path + [('fill y', x, j2)]) )
        if x > 0:
            queue.append(((0, y), path + [('empty x', 0, y)]) )
        if y > 0:
            queue.append(((x, 0), path + [('empty y', x, 0)]) )
        if x > 0 and y < j2:
            if x + y >= j2:
                queue.append(((x - (j2-y), j2), path + [('x to y', x - (j2-y), j2)]) )
            else:
                queue.append(((0, x + y), path + [('x to y', 0, x + y)]) )
        if x < j1 and y > 0:
            if x + y >= j1:
                queue.append(((j1, y - (j1-x)), path + [('y to x', j1, y - (j1-x))]) )
            else:
                queue.append(((x + y, 0), path + [('y to x', x + y, 0)]) )
    return None
start = (0, 0)
g=int(input("Enter the final capacity:"))
n=int(input("Enter the jar number:"))
if n==1:
    goal=(g,0)
elif n==2:
    goal=(0,g)
print("Given goal state is:",goal)
path = bfs(start, goal)
if path:
    print("Found a solution:")
    for step in path:
        print(step)
else:
    print("No solution found")'''

from collections import deque

def solve_bfs(x, y, target):
    queue = deque([(0, 0, [])])  # (x, y, path)
    visited = set()
    while queue:
        curr_x, curr_y, path = queue.popleft()
        if curr_x == target or curr_y == target:
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

bfs_solution = solve_bfs(4,3,2)
if bfs_solution:
    print("BFS solution:")
    for state in bfs_solution:
        print(state)
