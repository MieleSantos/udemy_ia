import streamlit as st
from page.controller.controller import ApiAudio

st.title("💬 Tradução de áudio!")

if "messages" in st.session_state:
    st.session_state.pop("messages")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Tradução de áudio! Faça upload do seu arquivo de áudio.",
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
    with st.spinner("Traduzindo áudio..."):
        response = ApiAudio().translations_audio(prompt)
        if response.status_code == 200:
            translations = response.json().get(
                "translations", "Erro ao traduzindo o áudio."
            )
            # st.success(f"Transcrição: {transcricao}")
            st.session_state.messages.append(
                {"role": "assistant", "content": translations}
            )
            st.chat_message("assistant").write(translations)
        else:
            st.error(f"Erro ao se comunicar com a API: {response.status_code}")
