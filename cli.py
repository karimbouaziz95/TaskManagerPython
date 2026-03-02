from functions import get_todos, write_todos
from datetime import datetime

now = datetime.now()

formatted = now.strftime("It is %B %d, %Y %H:%M:%S") 
print(formatted)

todos = get_todos()

while True:
    user_input = input("Type add, edit, complete, show or end: ").strip()

    if user_input.startswith("add") or user_input.startswith("new"):
        todo = user_input[4:] + "\n"
        todos.append(todo)

        write_todos(todos)

    elif user_input.startswith("show"):
        print(todos)
        for index, todo in enumerate(todos):
            print(index+1, "-", todo.strip())

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:].strip())
            index = number - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos[index] = new_todo

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_input.startswith("complete"):
            try:
                number = int(user_input[9:].strip())
                number = number - 1
                todo_to_remove = todos.pop(number).strip()
                print(f"Todo '{todo_to_remove}' was removed from the list.")
                write_todos(todos)
            except IndexError:
                print("There is no item with that number.")
                continue

    elif user_input.startswith("end"):
        break
    else:
        print("Command is not valid.")