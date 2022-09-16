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

lottie1=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_wytnbin0/ContactArrowButton.json")
st_lottie(lottie1,height=100,key='Projects')

code2="""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div class='social'>
        <div class="icons">
            <p> <i class="fa fa-envelope icon"></i><a href="mailto:saiswarup.yakkala@gmail.com">&nbsp saiswarup.yakkala@gmail.com </a></p>
            <p> <i class="fa material-icons">location_on</i>&nbsp Guntur AndhraPradesh</p>
            <p> <i class="fa fa-institution"></i>&nbsp SRM Institute of Science and Technology</p>
    </div>
    </br>
    <!-- Add font awesome icons -->
    <a href="https://github.com/SaiSwarup27" class="s fa fa-github"></a>
    <a href="https://www.linkedin.com/in/sai-swarup-yakkala-93258b209/" class="s fa fa-linkedin"></a>
    <a href="https://www.instagram.com/swarup__2_7/" class="s fa fa-instagram"></a>
    <a href="#" class="s fa fa-facebook"></a>
    <a href="#" class="s fa fa-twitter"></a>

    </div>
"""
st.markdown(code2,unsafe_allow_html=True)
st.markdown(bre,unsafe_allow_html=True)
















# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")
