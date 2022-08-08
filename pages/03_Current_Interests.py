import streamlit as st
from common_functions import txt
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# photos used
splunk_etl = Image.open('diagram_generation/splunk_etl.png')
st.title("Data Engineering")
st.sidebar.markdown("Data Engineering")

st.write("Architecture I've used in Course Work:")
st.write("Diagrams generated using diagrams python library")
gcp_image = Image.open('diagram_generation/gcp_services_architecture.png')
st.image(gcp_image, width=1000)


st.title("Architecture I've used with Clients")
