import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
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

lottie1=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_88z2psap.json")
st_lottie(lottie1,height=300,key='Experience')

#-----------------experience
st.subheader('Clubs and Activities')
co1,co2=st.columns(2)
with co1:
    st.write('##### Geeks for Geeks SRM')
    code1="""
    <div class='optizen'>
        <p> Technical Member (Machine Learning)</p>
        <div class='inneroptizen'>
            <p> 2022 present  </p>
                    <p> ↑  </p>
            <p>2021 October</p>
        </div>
    </div>
    """
    st.markdown(code1,unsafe_allow_html=True)
    st.markdown(bre,unsafe_allow_html=True)

    st.write('##### Next Gen AI SRM')
    code2="""
    <div class='optizen'>
        <p> Technical Member (NLP)</p>
        <div class='inneroptizen'>
            <p> 2022 present  </p>
                    <p> ↑  </p>
            <p>2022 April</p>
        </div>
    </div>
    """
    st.markdown(code2,unsafe_allow_html=True)
    st.markdown(bre,unsafe_allow_html=True)
with co2:
    st.write('##### Optizen SRM')
    code3="""
    <div class='optizen'>
        <p> Technical Member (Machine Learning)</p>
        <div class='inneroptizen'>
            <p> 2022 present  </p>
                    <p > ↑  </p>
            <p>2021 August</p>
        </div>
    </div>
    """
    st.markdown(code3,unsafe_allow_html=True)
    st.markdown(bre,unsafe_allow_html=True)

st.markdown(bre,unsafe_allow_html=True)
st.markdown(bre,unsafe_allow_html=True)
st.subheader('Intership')
col1,col2=st.columns(2)
with col1:
    st.write('##### Glocybs')
    code4="""
    <div class='optizen'>
        <p> Machine Learning Domain </p>
        <div class='inneroptizen'>
            <p> 2022 present  </p>
                    <p> ↑  </p>
            <p>2022 June</p>
        </div>
    </div>
    """
    st.markdown(code4,unsafe_allow_html=True)
    st.markdown(bre,unsafe_allow_html=True)
st.markdown(bre,unsafe_allow_html=True)













# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")
