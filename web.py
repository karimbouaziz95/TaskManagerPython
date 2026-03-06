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


for todo in todos:
    st.checkbox(todo)

st.text_input(
    label="", 
    placeholder="Enter a new todo...", 
    key="todo_input",
    on_change=add_todo
)

st.session_state