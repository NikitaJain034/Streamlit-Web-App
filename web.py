import streamlit as st
import functions as fn

todos = fn.get_todos()

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""
    
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fn.write_todos(todos)
    st.session_state["new_todo"] =""

st.title("To-Do App")
st.write("You can manage your tasks here.")

for index ,todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "Add new task:",key="new_todo",
              placeholder="Enter a new task here..."
              ,on_change=add_todo)

