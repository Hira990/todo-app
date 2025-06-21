import streamlit as st

st.title("📝 To-Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Naya task likho:")
if st.button("➕ Task add karo"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Please enter a task!")

st.subheader("📋 Tumhari To-Do List:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {task}")
else:
    st.info("Abhi koi task nahi hai.")

if st.button("🗑️ Saare tasks hatao"):
    st.session_state.tasks = []
    st.success("Saari list clear ho gayi!")