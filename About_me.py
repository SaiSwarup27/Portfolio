import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests

st.set_page_config(page_title='Portfolio',page_icon=("https://img.icons8.com/ios/2x/portfolio.png"),layout = 'wide', initial_sidebar_state = 'auto')

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie1=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_Fuxw3k.json")
lottie2=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_9kofhgky.json")
lottie3=load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_veaeyjlw.json")
lottie4=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_sltl9pyu.json")
lottie5=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json")

make_map_responsive= """
 <style>
 [title~="st.iframe"] { width: 100%}
 </style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)

























# ---- removing padding across website -----
remove_padding_css = """
    .block-container {
    padding: 0 1rem;
    }
    """
st.markdown(
    "<style>"
    + remove_padding_css
    + "</styles>",
    unsafe_allow_html=True,
    )
st.expander("foo")
st.markdown("""
        <style>
            .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
            .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# -----------------------------------------

line="""
    <hr color='white',padding=0>
    """

 # ---- about page ----

st_lottie(lottie2,height=100,key='hello')
st.write('_**Iam Sai Swarup**_')
about_me="""
<p style="font-family:"Source Code Pro";> A Frontend web developer and very much passionate 
on Machine learning and Deep learning. 

And having very good progromming skills on python
c, c++.

Working with my hands to make magic in my life </p>"""
column1,column2=st.columns([2,1])
with column1:
    st.markdown(about_me,unsafe_allow_html=True)
with column2:
    st_lottie(lottie5,height=200,key='coding')

st.markdown(line,unsafe_allow_html=True)

st.subheader('Technologies')
co1,co2,co3=st.columns(3)
with co1:
    with st.expander('Technical skills'):
        st.text('''Python    C    C++
Html    CSS    Javascript''')
with co2:
    with st.expander('Frame works'):
        st.text('''Tkinter   Opencv    Numpy
Pandas    Sklearn    NLTK    
TextBlob    Matplotlib    Keras
Streamlit    Pillow    Tensor flow 
Flask   ''')
with co3:
    with st.expander('Others'):
        st.text('''Excel    git    SQL
Arduino    VRML    Matlab       ''')



st.markdown(line,unsafe_allow_html=True)

st.subheader('Hobbies')
col1,col2=st.columns(2)
with col1:
    st.text('''Playing Chess
Listening Music
Exploring ideas and Knowledge
Clubs and Social Activities''')
with col2:
    st_lottie(lottie4,height=150,key='chess')
st.markdown(line,unsafe_allow_html=True)

#-------------------------------------

# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")


# ------ side bar ------


