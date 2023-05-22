j1=int(input("Enter j1 capacity:"))
j2=int(input("Enter j2 capacity:"))
def dfs(start, goal, visited, path):
    x, y = start
    if start == goal:
        return path
    if start in visited:
        return None
    visited.append(start)
    if x < j1:
        result = dfs((j1, y), goal, visited, path + [('fill x', j1, y)])
        if result:
            return result
    if y < j2:
        result = dfs((x, j2), goal, visited, path + [('fill y', x, j2)])
        if result:
            return result
    if x > 0:
        result = dfs((0, y), goal, visited, path + [('empty x', 0, y)])
        if result:
            return result
    if y > 0:
        result = dfs((x, 0), goal, visited, path + [('empty y', x, 0)])
        if result:
            return result
    if x > 0 and y < j2:
        if x + y >= j2:
            result = dfs((x - (j2-y), j2), goal, visited, path + [('x to y', x - (j2-y), j2)])
            if result:
                return result
        else:
            result = dfs((0, x + y), goal, visited, path + [('x to y', 0, x + y)])
            if result:
                return result
    if x < j1 and y > 0:
        if x + y >= j1:
            result = dfs((j1, y - (j1-x)), goal, visited, path + [('y to x', j1, y - (j1-x))])
            if result:
                return result
        else:
            result = dfs((x + y, 0), goal, visited, path + [('y to x', x + y, 0)])
            if result:
                return result
    return None
start = (0, 0)
start = (0, 0)
g=int(input("Enter the final capacity:"))
n=int(input("Enter the jar number:"))
if n==1:
    goal=(g,0)
elif n==2:
    goal=(0,g)
print("Given goal state is:",goal)
visited = []
path = dfs(start, goal, visited, [])
if path:
    print("Found a solution:")
    for step in path:
        print(step)
else:
    print("No solution found")

