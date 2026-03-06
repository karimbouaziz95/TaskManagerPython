import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do app built with Streamlit")
st.write("This app is a simple to-do list")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo...", key="todo_input")