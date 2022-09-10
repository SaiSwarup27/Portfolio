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
                    <p> A Deep Learning based Chat Bot  </p>
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
    
    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> Animal Intrusion Detection</p>
            <div class='innerproject'>
                    <p>Animal Detection using YOLOv5 </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Classifying various classes of animals using Yolov5 algorithm </p>
            <a href='https://github.com/SaiSwarup27/Animal-Intrusion-Detection'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Smart Pits</p>
            <div class='innerproject'>
                    <p>An IOT based project</p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Helps in increasing of ground water level by rain and taking safety precautions for the children from pits.</p>
            <a href='https://github.com/SaiSwarup27/Smart-Pits'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Tic Tac Toe</p>
            <div class='innerproject'>
                    <p>Tic-Tac-Toe game using Tkinter</p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Build Tic-Tac-Toe Game using Tkinter GUI</p>
            <a href='https://github.com/SaiSwarup27/Tic-Tac-Toe-using-Tkinter'> click here </a>
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
                    <p> A NLP based text auto correction and translation </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Correcting wrongly spelled words and translating into another language using TextBlob</p>
            <a href='https://github.com/SaiSwarup27/Text-Correction-and-translation'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> Crowd Prediction</p>
            <div class='innerproject'>
                    <p>Crowd prediction in gym using Random Forest Regressor</p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Crowd prediction in gym using Random Forest Regressor Algorithm</p>
            <a href='https://github.com/SaiSwarup27/Crowd-Prediction'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Damaged tree Detection</p>
            <div class='innerproject'>
                    <p>Detecting number of trees damaged </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Predicting environment loss after a natural disaster happens</p>
            <a href='https://github.com/SaiSwarup27/Damaged-tree-detection'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Counting Objects</p>
            <div class='innerproject'>
                    <p>Counting number of Objects using Python-OpenCV</p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Counting number of Objects using Python-OpenCV</p>
            <a href='https://github.com/SaiSwarup27/Counting-Objects'> click here </a>
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

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p> Language Detection</p>
            <div class='innerproject'>
                    <p> NLP Language detection </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>NLP Language detection using various Machine Learning Algorithms</p>
            <a href='https://github.com/SaiSwarup27/Language-detection'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Cryotherapy Classification</p>
            <div class='innerproject'>
                    <p>Classification of Cryotherapy dataset </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>Classification of Cryotherapy dataset using Logistic Regression algorithm</p>
            <a href='https://github.com/SaiSwarup27/Cryotherapy-Classification'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

    tab1,tab2=st.tabs(['project','Description'])
    with tab1:
        code1="""
        <div class='project'>
            <p>Glocybs Bot</p>
            <div class='innerproject'>
                    <p>A Deep Learning based Chat Bot </p>
            </div>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)
    with tab2:
        code1="""
        <div class='description'>
            <p>A speech-text and text-text conversational chat bot</p>
            <a href='https://github.com/GLOCYBS-COM/Chat-Bot'> click here </a>
        </div>
        """
        st.markdown(code1,unsafe_allow_html=True)
        st.markdown(bre,unsafe_allow_html=True)

























# --- external css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")
