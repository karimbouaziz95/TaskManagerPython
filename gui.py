import functions
import FreeSimpleGUI as sg

# Get the list of to-dos from the text file
todos = functions.get_todos()

# Define the GUI layout
label = sg.Text("Type in a to-do") 
input_box = sg.InputText(tooltip="Enter todo", key="TODO_INPUT") 
add_button = sg.Button("Add", key="ADD_TODO_BUTTON") 
list_box = sg.Listbox(values=todos, key="TODO_LIST", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", key="EDIT_TODO_BUTTON")
complete_button = sg.Button("Complete", key="COMPLETE_TODO_BUTTON")
exit_button = sg.Button("Exit", key="EXIT_BUTTON")

layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button],
    [complete_button, exit_button]
]

# Create the window and start the event loop
window = sg.Window("My To-Do App", layout=layout, font=("Helvetica", 20))
while True:
    event,values = window.read()

    # Handle window close event and other events
    if event == sg.WINDOW_CLOSED or event == "EXIT_BUTTON":
        break
    
    # Handle add button click
    elif event == "ADD_TODO_BUTTON":
        if values["TODO_INPUT"]:
            new_todo = values["TODO_INPUT"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["TODO_LIST"].update(values=todos)
        else:
            sg.popup("Please enter a to-do item before adding.", title="Input Error")

    # Handle edit button click
    elif event == "EDIT_TODO_BUTTON":
        if values["TODO_INPUT"]:
            todo_to_edit = values["TODO_LIST"][0]
            new_todo = values["TODO_INPUT"] + "\n"
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["TODO_LIST"].update(values=todos)
        else:            
            sg.popup("Please select a to-do item and enter the new text before editing.", title="Input Error")

    # Handle list box selection event
    elif event == "TODO_LIST" and values["TODO_LIST"]:
         window["TODO_INPUT"].update(value=values["TODO_LIST"][0])

    # Handle complete button click
    elif event == "COMPLETE_TODO_BUTTON":
        if values["TODO_LIST"]:
            todo_to_complete = values["TODO_LIST"][0]
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["TODO_LIST"].update(values=todos)
            window["TODO_INPUT"].update(value="")
        else:
            sg.popup("Please select a to-do item to complete.", title="Input Error")

    
    print("Event:", event)
    print("Values:", values)
    print(values["TODO_LIST"])

# Close the window when the loop ends
window.close()