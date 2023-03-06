def get_todos():
    with open('todos.txt', 'r') as filet:
        todos_list = filet.readlines()
    return todos_list