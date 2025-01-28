import streamlit as st

from page.controller.controller import ApiText

st.title("💬 Moderação de conteúdo")
if "messages" in st.session_state:
    st.session_state.pop("messages")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Como posso ajudar você?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = ApiText().moderactions(prompt)
    if not response:
        st.error("Erro ao se comunicar com a API):")
    elif response.json().get("moderacao"):
        response = response.json().get("moderacao")

        sd = ", ".join(i for i in response.keys())
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(f"Conteúdo classificado como: {sd}")
    else:
        st.chat_message("assistant").write("Conteúdo moderado com sucesso!")
