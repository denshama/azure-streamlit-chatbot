import streamlit as st
import yaml
with open('./config.yml', 'r') as file:
    config = yaml.safe_load(file)

st.set_page_config(
    page_title=config['streamlit']['tab_title'], 
    page_icon=config['streamlit']['page_icon'], 
    )
st.image(config['streamlit']['logo'], width=200)
pg = st.navigation([
#    st.image(config['streamlit']['logo'], width=200),
    st.Page("main.py", title="Mail Generator"),
    st.Page("translate.py", title="Leica Translator"),
])
pg.run()