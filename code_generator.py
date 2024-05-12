import random
import pandas as pd
from random_strings import *


def generate_random_variable_name():
    return random.choice(variable_names)

def generate_random_value():
    return str(random.randint(1, 100))

def generate_df():
    df_dictionnary = {}
    num_lines = random.randint(5,15)
    for _ in range(random.randint(5,15)):
        values = [generate_random_value() for i in range(num_lines)]
        df_dictionnary[generate_random_variable_name()] = values
    return pd.DataFrame(data=df_dictionnary)


def generate_df_code_line():
    newDfName = 'df' + str(random.getrandbits(random.randint(1,5)))
    return f'{newDfName} = ' + 'df.' + random.choice(operations)

def insert_content_at_line(file_path, line_number, content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if 'for' in lines[line_number-2]:
        lines.insert(line_number - 1, ' ' + content + '\n') 
    else: 
        lines.insert(line_number - 1, content + '\n')

    with open(file_path, 'w') as file:
        file.writelines(lines)
        
def commit_message_generator():
    return random.choice(commit_messages)




# def generate_random_assignment():
#     variable = generate_random_variable_name()
#     value = generate_random_value()
#     return f'{variable} = {value}'


# def generate_random_variable_declaration():
#     code_snippet = []
#     num_statements = random.randint(1, 5)

#     for _ in range(num_statements):
#         statement_type = random.choice(['variable_declaration', 'assignment'])
        
#         if statement_type == 'variable_declaration':
#             variable = generate_random_variable_name()
#             code_snippet.append(f'let {variable};')
#         elif statement_type == 'assignment':
#             assignment = generate_random_assignment()
#             code_snippet.append(assignment)

#     return '\n'.join(code_snippet)

# if __name__ == '__main__':
#     random_code = generate_random_code_snippet()
#     print(random_code)
