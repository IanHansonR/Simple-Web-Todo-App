FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text file and return list of items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write items to the text file for storage."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_goals(filepath="goals.txt"):
    """Read text file and return list of items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_goals(goals_arg, filepath="goals.txt"):
    """Write items to the text file for storage."""
    with open(filepath, 'w') as file:
        file.writelines(goals_arg)

def get_format(user_input_local):
    """Capitalizes  first letter of first word in user's input"""
    input_list = user_input_local.split(" ")
    cap = input_list[0].title()
    input_list[0] = cap
    formatted_input = " ".join(input_list)
    return formatted_input


if __name__ == "__main__":
    user_input = "surfing every day"
    formatted = get_format(user_input)
    print(formatted)