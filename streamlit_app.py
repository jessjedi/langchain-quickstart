import streamlit as st
from langchain.llms import OpenAI
from st_audiorec import st_audiorec
import pandas as pd
from io import StringIO

LOGO_URL_SMALL = '/Users/jessicasnare/Downloads/Social Media Posts-3.png'
st.set_page_config(page_title="Conversense")
st.title('Welcome to Converscense!')

st.logo(
    LOGO_URL_SMALL,
    size = "large",
    link="https://streamlit.io/gallery",
    icon_image=None,
)

home_page = st.Page("create.py", title="Home", icon=None)
chat_with_cashew_page = st.Page("delete.py", title="Chat with Cashew", icon=None)
explore_page = st.Page("delete.py", title="Explore", icon=None)

pg = st.navigation([home_page, chat_with_cashew_page, explore_page])
st.set_page_config(page_title="Home", page_icon=None)
pg.run()

#wav_audio_data = st_audiorec()

#if wav_audio_data is not None:
#st.audio(wav_audio_data, format='audio/wav')

#uploaded_file = st.file_uploader("Choose a file")

# Allow users to upload video files (e.g., .mp4, .mov)
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])

if uploaded_file is not None:
    # To read file as bytes:
    video_bytes = uploaded_file.getvalue()
    
    # Show the uploaded video file size (for feedback to user)
    st.write(f"Video file size: {len(video_bytes)} bytes")
    
    # Optionally, you can display the video directly within Streamlit
    st.video(video_bytes)
    
    # If you need to save this video into a variable to use later:
    video_data = video_bytes  # This variable holds the video in byte format
    
    # Additional processing can be done on video_data as needed.
    # For example, saving it to a file on the server:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_data)
    st.write("Video submited successfully.")

st.divider()
st.title('Next Step: Wait for the Magic 🪄')
