# Content from ~/streamlit_apps/main_page.py
import streamlit as st
from PIL import Image

image = Image.open('Colin_image.jpg')
st.image(image, width=150)

st.header("Colin Best Resume")

st.markdown("Main Page")
st.sidebar.markdown("# Main page 🎈")
