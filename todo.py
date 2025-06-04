

import streamlit as st

# App title
st.title("✅ To-Do List App")

# Initialize task list in session_state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to display and manage tasks
def show_tasks():
    st.subheader("Your Tasks:")

    if not st.session_state.tasks:
        st.info("🎉 No tasks yet. Add one above!")
        return

    remove_indices = []
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.checkbox(task, key=f"task_{i}")
        with col2:
            if st.button("❌", key=f"del_{i}"):
                remove_indices.append(i)

    # Remove marked tasks
    for i in sorted(remove_indices, reverse=True):
        del st.session_state.tasks[i]

# Input section
st.subheader("Add a new task:")
new_task = st.text_input("Enter task", "")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success("Task added!")
    else:
        st.warning("Please enter a task.")

# Show current tasks
show_tasks()

# Clear all button
if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks cleared!")
