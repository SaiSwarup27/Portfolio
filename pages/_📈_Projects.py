import streamlit as st
from streamlit_lottie import st_lottie
import requests

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
bre="""
    </br>
    """
# -----------------------------------------

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie1=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_16MhZz.json")
st_lottie(lottie1,height=300,key='Projects')

#-----------------------------------
col1,col2,col3=st.columns(3)
with col1:
    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> NLP Chat bot</p>
            <div class='innerproject'>
                    <p> A Deep Learning </br> based Chat Bot  </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Which helps you to clarify doubts based on NLP </p>
            <a href='https://github.com/SaiSwarup27/NLP-ChatBot'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

with col2:
    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> Text Correction and Translation</p>
            <div class='innerproject'>
                    <p> A Deep Learning </br> based Chat Bot  </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Which helps you to clarify doubts based on NLP </p>
            <a href='https://github.com/SaiSwarup27/NLP-ChatBot'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

with col3:
    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> Digital Diner</p>
            <div class='innerproject'>
                    <p> A responsive restaurant website build using html and css.  </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Helps the user to navigate quickly from one category to another category of foods.</p>
            <a href='https://github.com/SaiSwarup27/Digital-Diner'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
























# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")
