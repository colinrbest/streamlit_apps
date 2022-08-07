# Content from ~/streamlit_apps/main_page.py
import streamlit as st
from PIL import Image
from common_functions import txt

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
splunk_etl = Image.open('diagram_generation/splunk_etl.png')

# first column grouping
col1, col2, col3 = st.columns(3)

with col1:
    image = Image.open('Colin_image.jpg')
    st.image(image, width=150)
with col3:
    st.header("Colin Best Technical Resume")

st.markdown('## Summary', unsafe_allow_html=True)
st.markdown('###### Unlike my traditional resume where I have focused on outcomes, I wanted to use this website to display my technical skills in more detail as well as display project architecture', unsafe_allow_html=True)
st.info('''
- Experienced Data Scientist/Data Engineer with strong presentation and project management skills.
- M.S. Data Science with 5 Years of Telecommunications experience, 4 years experience working in public cloud environments. 
- Interested in all things Data Science, Cybersecurity, and Application Development. 
''')
#####################
# Navigation

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    color: #66B2FF;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


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

#####################
st.markdown('''
## Education
''')

txt('**M.S. Data Science** University of Notre Dame',
    '2018-2020')
st.markdown('''
- Assisted a medical communications company with improving client research efficiency in a Capstone project
- `Developed proprietary natural language processing techniques to improve research in new therapeutic areas`
- Courses in: `Statistical Learning, Generalized Linear Models, Behavioral Data Science, Data Visualization`
''')

txt('**Bachelors of Arts**, *University of Virginia*',
    '2012-2015')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `Splunk`, `Datadog`')
txt3('Data visualization',
     '`matplotlib`, `seaborn`, `plotly`, `ggplot2`, `Tableau`, `PowerBI`, `Data Studio`, `Streamlit`')
txt3('Machine Learning',
     '`Tensorflow`,`scikit-learn`, `Vertex AI Platform`, `AWS Sagemaker`')
txt3('Coursera Courses Completed:', '`DeepLearning.AI TensorFlow Developer`,`Building Resilient Streaming Analytics Systems on Google Cloud`, `MLOps (Machine Learning Operations) Fundamentals`, `Smart Analytics, Machine Learning, and AI on GCP`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/colin-best-18960370/')
