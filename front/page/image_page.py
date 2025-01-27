import streamlit as st
from page.controller.controller import Api

st.title("💬 Criação de image")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = Api().create_image(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
    # st.chat_message("assistant").write(st.image(response, use_column_width=True))
    st.image(response, use_container_width=True)
