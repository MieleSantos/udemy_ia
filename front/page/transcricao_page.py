import streamlit as st
from page.controller.controller import Api

st.title("💬 Trascrição de áudio!")

if "messages" in st.session_state:
    st.session_state.pop("messages")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Trascrição de áudio! Faça upload do seu arquivo de áudio.",
        }
    ]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.file_uploader(
    " ",
    type=["mp3"],
):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # st.chat_message("assistant").write("Transcrevendo áudio...")
    with st.spinner("Transcrevendo áudio..."):
        response = Api().transcribe_audio(prompt)
        if response.status_code == 200:
            transcricao = response.json().get(
                "transcricao", "Erro ao transcrever o áudio."
            )
            # st.success(f"Transcrição: {transcricao}")
            st.session_state.messages.append(
                {"role": "assistant", "content": transcricao}
            )
            st.chat_message("assistant").write(transcricao)
        else:
            st.error(f"Erro ao se comunicar com a API: {response.status_code}")
