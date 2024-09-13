import streamlit as st
import yaml
from llm_bot import translate

# Read config yaml file
with open('./config.yml', 'r') as file:
    config = yaml.safe_load(file)
#print(config)

title = config['translate']['title']
avatar = {
    'user': None,
    'assistant': config['translate']['avatar']
}

# Set page config

pg = st.navigation([
    st.Page("main.py", title="Mail Generator"),
    st.Page("translate.py", title="Leica Translator"),
])

# Set sidebar
#st.sidebar.title("About")
#st.sidebar.info(config['translate']['about'])

# Set logo
#st.image(config['translate']['logo'], width=200)

# Set page title
st.title(title)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [] 
    st.session_state.messages.append({
        "role": "assistant", 
        "content": config['translate']['assistant_intro_message']
        })

# Display chat messages from history on app rerun
#for message in st.session_state.messages:
#    with st.chat_message(message["role"], avatar=avatar[message["role"]]):
#        st.markdown(message["content"])
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True, height=500):
         froml = st.selectbox("Language From", ("English (US)", "German", "French", "Spanish (International)", "Italian", "Portuguese (Brasil)", "Chinese", "Korean", "Japanese", "Klingon", "Klingon (plqaD)")), 
         source = st.text_area("", "tell me about leica products")
with col2:
        with st.container(border=True, height=500):
            tol = st.selectbox("Language To", ("English (US)", "German", "French", "Spanish (International)", "Italian", "Portuguese (Brasil)", "Chinese", "Korean", "Japanese", "Klingon", "Klingon (plqaD)"), 1)
            if st.button("Translate"):
                    st.markdown(translate(source, froml, tol))
                    st.balloons()

