import random

def generate_random_variable_name():
    variable_names = ['x', 'y', 'z', 'foo', 'bar', 'baz', 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'theta', 'omega', 'variable1', 'variable2', 'variable3', 'index', 'count', 'result', 'value']
    return random.choice(variable_names)

def generate_random_value():
    return str(random.randint(1, 100))

def generate_random_assignment():
    variable = generate_random_variable_name()
    value = generate_random_value()
    return f'{variable} = {value}'

def generate_random_code_snippet():
    code_snippet = []
    num_statements = random.randint(1, 5)

    for _ in range(num_statements):
        statement_type = random.choice(['variable_declaration', 'assignment'])
        
        if statement_type == 'variable_declaration':
            variable = generate_random_variable_name()
            code_snippet.append(f'let {variable};')
        elif statement_type == 'assignment':
            assignment = generate_random_assignment()
            code_snippet.append(assignment)

    return '\n'.join(code_snippet)

if __name__ == '__main__':
    random_code = generate_random_code_snippet()
    print(random_code)
