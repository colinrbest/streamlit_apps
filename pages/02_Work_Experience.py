import streamlit as st
from common_functions import txt
from PIL import Image
from common_functions import txt, txt2, txt3, img_to_bytes

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# photos used
splunk_etl = Image.open('diagram_generation/splunk_etl.png')
reports = Image.open('diagram_generation/reporting.png')

st.sidebar.markdown("Accenture, AT&T, RiskLens")


#####################
st.markdown('''
## Work Experience
''')

txt('**Data Science Consultant**, Accenture, Denver, Colorado', '2021-Present')

st.markdown('''
- Telecommunications Client
- Worked across several roles as a Data Engineer, Data Scientist, and Team Lead on an Operational Intelligence Platform
- Click the tabs below to see different tools and architectures used for this work
''')
tab1, tab2, tab3 = st.tabs(
    ["Tools Used", "ETL Architecture", "Reporting Architecture"])

with tab1:
    st.markdown('''
    - ETL: `Python, Linux, Chrontab, Splunk Query Language (SPL), Datadog API, SQL, Kafka`
    - Reporting: `SQL, Python, Jupyter notebooks, Papermill, Chrontab, Seaborn, Streamlit`
    ''')

with tab2:
    st.header("Example of one ETL process with log records from Splunk")
    st.image(splunk_etl, width=1000)

with tab3:
    st.header("Example Daily Report that would run")
    st.image(reports, width=1000)
