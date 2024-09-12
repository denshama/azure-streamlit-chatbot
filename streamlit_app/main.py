import streamlit as st
import yaml
from llm_bot import createmail

# Read config yaml file
with open('./streamlit_app/config.yml', 'r') as file:
    config = yaml.safe_load(file)
#print(config)
title = config['streamlit']['title']
avatar = {
    'user': None,
    'assistant': config['streamlit']['avatar']
}

# Set page config
st.set_page_config(
    page_title=config['streamlit']['tab_title'], 
    page_icon=config['streamlit']['page_icon'], 
    )

# Set sidebar
#st.sidebar.title("About")
#st.sidebar.info(config['streamlit']['about'])

# Set logo
st.image(config['streamlit']['logo'], width=200)

# Set page title
st.title(title)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [] 
    st.session_state.messages.append({
        "role": "assistant", 
        "content": config['streamlit']['assistant_intro_message']
        })

# Display chat messages from history on app rerun
#for message in st.session_state.messages:
#    with st.chat_message(message["role"], avatar=avatar[message["role"]]):
#        st.markdown(message["content"])
col1, col2 = st.columns(2)
with col1:
    content = st.text_input("Content", "tell me about leica products")
    product = st.text_input("Product", "Stellaris 8")
    about = st.text_input("About","best solution for cancer research, rapid procedures, flexibility and manoeuvrability")
    action = st.text_input("Call to Action","call your salerep now for enhanced discount")
with col2:
    role = st.text_input("Role", "Microsopy Expert")
    persona = st.text_input("Persona", "Buying Manager")
    painpoint = st.text_input("Painpoint", "maximize use of systems, simplify workflows, better medical outcomes")
    length = st.text_input("Number of Words", "250")
    language = st.text_input("language", "English")

if st.button("Create Email"):
    with st.expander("Email Created"):
        st.markdown(createmail(content, product, about, action, role, persona, painpoint, length, language))



