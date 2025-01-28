import streamlit as st


pages = {
    "Chat de texto": [
        st.Page("page/text_page.py", title="Chatbot", icon=":material/chat:"),
        st.Page(
            "page/moderation_page.py",
            title="Moderação de texto",
            icon=":material/chat:",
        ),
        st.Page(
            "page/image_page.py",
            title="Crieção de imagem",
            icon=":material/chat:",
        ),
    ],
    "Chat de audio": [
        st.Page(
            "page/transcricao_page.py",
            title="Transcrição de audio",
            icon=":material/chat:",
        ),
        st.Page(
            "page/translations_page.py",
            title="Transcrição de audio",
            icon=":material/chat:",
        ),
    ],
}

pg = st.navigation(pages)
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
