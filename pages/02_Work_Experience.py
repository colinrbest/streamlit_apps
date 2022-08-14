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
# ACN Experience
txt('**Data Science Consultant**, Accenture, Denver, Colorado', '2021-Present')

st.markdown('''
- Telecommunications Client
- Worked across several roles as a Data Engineer, Data Scientist, and Team Lead on an Operational Intelligence Platform
- Click the tabs below to see different tools and architectures used for this work
''')
tab1_acn, tab2_acn, tab3_acn = st.tabs(
    ["Tools Used", "ETL Architecture", "Reporting Architecture"])

with tab1_acn:
    st.markdown('''
    - ETL: `Python, Linux, Chrontab, Splunk Query Language (SPL), Datadog API, SQL, Kafka`
    - Reporting: `SQL, Python, Jupyter notebooks, Papermill, Chrontab, Seaborn, Streamlit`
    ''')

with tab2_acn:
    st.header("Example of one ETL process with log records from Splunk")
    st.image(splunk_etl, width=1000)

with tab3_acn:
    st.header("Example Daily Report that would run")
    st.image(reports, width=1000)

# AT&T Experience
txt('**Data Scientist - Professional Cybersecurity**, AT&T, Dallas, Texas', '2019-2020')

st.markdown('''
- KRIs, KPIs, and executive vulnerability reporting to the Chief Security Officer
- UX Analytics to drive cybersecurity product roadmap and feature enhancements
- VPC Security group recommendation engine for improving security posture
- Click the tabs below to see different tools and architectures used for this work
''')
tab1_att, tab2_att, tab3_att = st.tabs(
    ["Tools Used", "KRI/KPI Reporting", "UX Analytics", "VPC Rec Engine"])

with tab1_att:
    st.markdown('''
    - ETL: `Python, Linux, Chrontab, Splunk Query Language (SPL), Datadog API, SQL, Kafka`
    - Reporting: `SQL, Python, Jupyter notebooks, Papermill, Chrontab, Seaborn, Streamlit`
    ''')

with tab2_att:
    st.header("Example of one ETL process with log records from Splunk")
    st.image(splunk_etl, width=1000)

with tab3_att:
    st.header("Example Daily Report that would run")
    st.image(reports, width=1000)
