#Implement the A* Algorithm to find the shortest path between 2 points on a 2D grid with obstacles

from queue import PriorityQueue
def heuristic(point, goal):
  return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
def astar(start, goal, obstacles):
    """
    Returns the shortest path between start and goal on a 2D grid with obstacles using the A* algorithm.
    """
    # Define a heuristic function that estimates the distance from any point to the goal
    

    # Initialize the set of visited points and the priority queue of points to explore
    visited = set()
    frontier = PriorityQueue()
    frontier.put((heuristic(start, goal), start, [], 0))
    while not frontier.empty():
        # Get the next point to explore
        f_value, current, path, g_value = frontier.get()

        # Check if the goal has been reached
        if current == goal:
            return path + [current]

        # Check if the current point is an obstacle or has already been visited
        if current in visited or current in obstacles:
            continue

        # Mark the current point as visited
        visited.add(current)

        # Add the neighbors of the current point to the frontier
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            new_g_value = g_value + 1
            if neighbor not in visited:
                frontier.put((new_g_value + heuristic(neighbor, goal), neighbor, path + [current], new_g_value))

    # Return None if no path is found
    return None
# Define the start and goal points and the set of obstacles
start = (0, 0)
goal = (3, 3)
print("Goal State:",goal)
obstacles = [(1, 2), (2, 2), (3, 2),(2,4)]
print("Obstacles:",obstacles)
path = astar(start, goal, obstacles)

# Print the path
if path is None:
    print("No path found.\n")
else:
    print("Shortest path:\n", path)

