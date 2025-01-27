import streamlit as st

chat_text_page = st.Page(
    "page/text_page.py", title="Chatbot", icon=":material/add_circle:"
)
image_create_page = st.Page(
    "page/image_page.py", title="Create image", icon=":material/add_circle:"
)


pg = st.navigation([chat_text_page, image_create_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()
