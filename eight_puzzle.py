from heapq import heappop, heappush

def solve_8puzzle(initial_state):
    goal_state = "12345678_"
    moves = {"U": -3, "D": 3, "L": -1, "R": 1}

    open_list, closed_set = [], set()
    priority = lambda state, cost: cost + heuristic(state)

    cost = 0
    heappush(open_list, (priority(initial_state, cost), cost, initial_state))

    while open_list:
        _, cost, current_state = heappop(open_list)
        closed_set.add(current_state)
        print_state(current_state)
        if current_state == goal_state:
            print("Solution found in", cost, "moves.")
            return 

        zero_index = current_state.index("_")

        for move, step in moves.items():
            new_index = zero_index + step
            if 0 <= new_index < 9 and (move != "L" or zero_index % 3 != 0) and (move != "R" or zero_index % 3 != 2):
                new_state = list(current_state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = "".join(new_state)

                if new_state not in closed_set:
                    heappush(open_list, (priority(new_state, cost + 1), cost + 1, new_state))
            
    print("No solution found.")
    
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
    
def heuristic(state):
    goal_state = "12345678_"
    misplaced = sum(s1 != s2 for s1, s2 in zip(state, goal_state))
    return misplaced

initial_state = "1_3425786"
solve_8puzzle(initial_state)
