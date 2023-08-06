import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if st.session_state.new_todo:
        todos.append(st.session_state.new_todo + "\n")
        functions.write_todos(todos)
        st.session_state.new_todo = ""


st.title("My Todos:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

new_todo_text = st.text_input("", placeholder="Add a new todo...",
                              key='new_todo', on_change=add_todo)

