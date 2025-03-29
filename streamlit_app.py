import streamlit as st
from langchain.llms import OpenAI
from st_audiorec import st_audiorec
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Conversense")


pg = st.navigation([st.Page("home.py"), st.Page("chat.py")])


home_page = st.Page("home.py", title="Home", icon=None)
chat_with_cashew_page = st.Page("chat.py", title="Chat with Cashew", icon=None)
pg.run()


#wav_audio_data = st_audiorec()

#if wav_audio_data is not None:
#st.audio(wav_audio_data, format='audio/wav')

#uploaded_file = st.file_uploader("Choose a file")


