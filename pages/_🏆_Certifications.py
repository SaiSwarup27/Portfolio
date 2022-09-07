import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import webbrowser


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie1=load_lottieurl('https://lottie.host/e5b3b6ba-fe5e-46c5-8737-04ee01d21226/xoMKxSfrS1.json')
st_lottie(lottie1,height=100,key='certificate')

#----------------------------------------
st.subheader('Certifications')

url1 = 'https://drive.google.com/file/d/1slHDA6ZuAmXT8scbzFYAHHq03HEUkjwe/view?usp=sharing'
url2 = 'https://drive.google.com/file/d/1zkQXg5upuDK64ZJZJLGkDkOKTGSWbL3L/view?usp=sharing'
url3 = 'https://drive.google.com/file/d/180WUlAkYJdBqoEcvzSVEk7s4a4xZGx1P/view?usp=sharing'
url4 = 'https://drive.google.com/file/d/1jbIok_Gdb_-vt4z3f8s7WZ1yILPun1lA/view?usp=sharing'
url5 = 'https://drive.google.com/file/d/1LlVcHqxUd9F7vxHODUr7pdZATxrgpRSZ/view?usp=sharing'
url11 = ''
url12 = ''
url13 = ''

if st.button('Enduro Python certificate from IIT Kharagpur'):
    webbrowser.open_new(url1)
if st.button('Coursera Web App with Python and Flask'):
    webbrowser.open_new(url2)
if st.button('Linkedin Learning Data Analytics'):
    webbrowser.open(url3)
if st.button('Teachnook AI Internship'):
    webbrowser.open_new_tab(url4)
if st.button('Teachnook AI Course Completion'):
    webbrowser.open_new_tab(url5)
if st.button('Coursera Web development'):
    webbrowser.open_new_tab(url11)
if st.button('Coursera Introduction to Machine Learning'):
    webbrowser.open_new_tab(url12)
if st.button('Coursera Deep Learning Techniques'):
    webbrowser.open_new_tab(url13)
st.text("""

""")
st.subheader('Competitions and Hackathons')
url6 = 'https://drive.google.com/file/d/15nZci86bTPKDVS4PljXSep1_nmPrjaOC/view?usp=sharing'
url7 = 'https://drive.google.com/file/d/1emwgkE5NkzpDAySlzie5CnXsQUMuWTot/view?usp=sharing'
url8 = 'https://drive.google.com/file/d/1mUHO9ZiZdXiHmAaJQzEx6P5he13lmfRJ/view?usp=sharing'
url9 = 'https://drive.google.com/file/d/1wVxGxFlkncicoykdYrqe8EVf-FUWGD44/view?usp=sharing'
url10 = 'https://drive.google.com/file/d/1EugIWGZQ8MubnK6shQIlDTvO55qILJ7P/view?usp=sharing'

if st.button('Hack Trix Take 2 Hackathon'):
    webbrowser.open_new_tab(url6)
if st.button('GUVI Computer Programming'):
    webbrowser.open_new_tab(url7)
if st.button('Codechef SnackDown 2021'):
    webbrowser.open_new_tab(url8)
if st.button('NVIDIA Building Transformer Based NLP'):
    webbrowser.open_new_tab(url9)
if st.button('NVIDIA Fundamentals of Deep Learning'):
    webbrowser.open_new_tab(url10)





# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

