import streamlit as st
from common_functions import txt

st.markdown("Work Experience")
st.sidebar.markdown("Work Experience")


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
tab1, tab2, tab3, tab4 = st.tabs(["Tools Used", "ETL Architecture",
                                  "Data Science Architecture", "Reporting Architecture"])

with tab1:
    st.markdown('''
    - ETL: `Python, Linux, Chrontab, Splunk Query Language (SPL), Datadog API, SQL, Kafka`
    - Reporting: `SQL, Python, Jupyter notebooks, Papermill, Chrontab, Seaborn, Streamlit`
    ''')

with tab2:
    st.header("Example of one ETL process with log records from Splunk")
    st.image(splunk_etl, width=700)
