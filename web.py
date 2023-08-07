import streamlit as st
import functions

todos = functions.get_todos()
goals = functions.get_goals()


def add_todo():
    if st.session_state.new_todo:
        todos.append(st.session_state.new_todo + "\n")
        functions.write_todos(todos)
        st.session_state.new_todo = ""


def add_goal():
    if st.session_state.new_goal:
        goals.append(st.session_state.new_goal + "\n")
        functions.write_goals(goals)
        st.session_state.new_goal = ""


st.subheader("Focus:")
for index, goal in enumerate(goals):
    checkbox = st.checkbox(goal, key=goal)
if st.button("Delete Goal"):
    if st.session_state:
        goals.pop()
        functions.write_goals(goals)
        st.experimental_rerun()
new_goal = st.text_input('', placeholder='Enter a goal...', key='new_goal',
                         on_change=add_goal)


st.title("My Todos:")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

new_todo_text = st.text_input("", placeholder="Add a new todo...",
                              key='new_todo', on_change=add_todo)

