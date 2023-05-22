reward = -0.01
discount = 0.5
max_error = 1e-3
num_actions = 4
actions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

num_row = 3
num_col = 4
U = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]

def getU(U, r, c, action):
    dr, dc = actions[action]
    newR, newC = r + dr, c + dc
    if newR < 0 or newC < 0 or newR >= num_row or newC >= num_col or (newR == newC == 1):
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(U, r, c, action):
    u = reward
    u += 0.1 * discount * getU(U, r, c, (action - 1) % 4)
    u += 0.8 * discount * getU(U, r, c, action)
    u += 0.1 * discount * getU(U, r, c, (action + 1) % 4)
    return u

def valueIteration(U):
    print("The initial state is:")
    for row in U:
        print(" | ".join(f"{val:5}" for val in row))
    print("\nDuring the value iteration:")
    iteration = 0
    while True:
        nextU = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
        error = 0
        for r in range(num_row):
            for c in range(num_col):
                if (r <= 1 and c == 3) or (r == c == 1):
                    continue
                nextU[r][c] = max([calculateU(U, r, c, action) for action in range(num_actions)])
                error = max(error, abs(nextU[r][c] - U[r][c]))
        U = nextU
        for row in U:
            print(" | ".join(f"{val:5.2f}" for val in row))
        print()
        iteration += 1
        if error < max_error or iteration > 10:  # Stop condition modified for faster execution
            break
    return U

U = valueIteration(U)
print("\nThe optimal policy is:")
for row in U:
    print(" | ".join(f"{val:5.2f}" for val in row))
