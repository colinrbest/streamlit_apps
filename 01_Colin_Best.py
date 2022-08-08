# Content from ~/streamlit_apps/main_page.py
import streamlit as st
from PIL import Image
from common_functions import txt, txt2, txt3, img_to_bytes

# CSS style sheet
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# bootstrap
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Photos used
splunk_etl = Image.open('diagram_generation/splunk_etl.png')

# Header for Document
st.markdown("<h1 style='text-align: center; color: black;'>Colin Best Technical Resume</h1>",
            unsafe_allow_html=True)

image = Image.open('Colin_image.jpg')
st.image(image, width=150)


# Start of page
st.markdown('## Summary', unsafe_allow_html=True)
st.markdown('###### Unlike my traditional resume where I have focused on outcomes, I wanted to use this website to display my technical skills in more detail as well as display project architecture', unsafe_allow_html=True)
st.info('''
- Experienced Data Scientist/Data Engineer with strong presentation and project management skills.
- M.S. Data Science with 5 Years of Telecommunications experience, 4 years experience working in public cloud environments. 
- Interested in all things Data Science, Cybersecurity, and Application Development. 
''')
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
st.markdown("""
- <a class="navbar-brand" href="https://www.canva.com/design/DAD4hV6pkng/rgtTJdCrqTA8r9P3xSIxmQ/view?utm_content=DAD4hV6pkng&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" target="_blank">Checkout my Final Report Here</a>
    """, unsafe_allow_html=True)


txt('**Bachelors of Arts**, *University of Virginia*',
    '2012-2015')
st.markdown('''
- Major in Foreign Affairs with a Minor in French 
- Member of the Jefferson Literary and Debate Society, the oldest club of its kind in the United States.
''')


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
