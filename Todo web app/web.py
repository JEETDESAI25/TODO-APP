import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app is useful to increase your productivity.")
st.write("Here are your Todo's.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox is True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a Todo", on_change=add_todo, key="new todo")
