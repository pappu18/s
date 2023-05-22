from simpleai.search import CspProblem, backtrack
def constraint_func(names, values):
    return values[0] != values[1]
if __name__ == '__main__':
    names = ('Ma', 'Ju', 'St', 'Am', 'Br', 'Jo', 'De', 'Al', 'Mi', 'Ke')
    colors = dict((name, ['red', 'green', 'blue', 'gray']) for name in names)
    constraints = [
        (('Ma', 'Ju'), constraint_func),
        (('Ma', 'St'), constraint_func),
        (('Ju', 'St'), constraint_func),
        # ... additional constraints ...
    ]
    problem = CspProblem(names, colors, constraints)
    output = backtrack(problem)
    print('\nColor mapping:\n')
    for k, v in output.items():
        print(k, '==>', v)
