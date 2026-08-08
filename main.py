import streamlit as st
pagina_chat = st.Page("chat_view.py", title="Consultor SENAI", default=True, icon="🧠") 
pagina_admin = st.Page("admin_view.py", title="Painel do Admin", icon="🧠")

pg = st.navigation({
    "Atendimento" : [pagina_chat],
    "Gerenciamento": [pagina_admin]
})

pg.run()