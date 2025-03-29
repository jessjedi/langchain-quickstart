import streamlit as st

st.title("Welcome to Conversense!")
st.subheader("We are sooooooo excited to meet you! Are you excited to get started?")

if st.button("YES!"):
    st.balloons()
    st.subheader("Perfect! Let's get started. Click the Chat page to continue")

st.image('/Users/jessicasnare/Desktop/Hack/Hack25.png', caption=None, width=200)