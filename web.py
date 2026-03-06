import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state["todo_input"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    #st.session_state["todo_input"] = ""

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do app built with Streamlit")
st.write("This app is a simple to-do list")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="", 
    placeholder="Enter a new todo...", 
    key="todo_input",
    on_change=add_todo
)

st.session_state