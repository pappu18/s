def solve_memoization(x, y, target, curr_x, curr_y, memo):
    if (curr_x == target and curr_y==0) or (curr_x==0 and curr_y == target):
        return [(curr_x, curr_y)]

    if (curr_x, curr_y) in memo:
        return None

    memo.add((curr_x, curr_y))

    operations = [
        ('Fill X', x, curr_y),
        ('Fill Y', curr_x, y),
        ('Empty X', 0, curr_y),
        ('Empty Y', curr_x, 0),
        ('Pour X to Y', max(0, curr_x + curr_y - y), min(y, curr_x + curr_y)),
        ('Pour Y to X', min(x, curr_x + curr_y), max(0, curr_x + curr_y - x))
    ]

    for operation, next_x, next_y in operations:
        result = solve_memoization(x, y, target, next_x, next_y, memo)
        if result is not None:
            return [(curr_x, curr_y, operation)] + result

    return None

memo_solution = solve_memoization(x_capacity, y_capacity, target_amount, 0, 0, set())
if memo_solution:
    print("\nMemoization solution:")
    for state in memo_solution:
        print(state)
else:
    print("No solution")
