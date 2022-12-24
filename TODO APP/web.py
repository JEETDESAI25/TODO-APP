import streamlit as st
import functions 

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to useful to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a Todo",on_change=add_todo, key="new todo")



st.session_state