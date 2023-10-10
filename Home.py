import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.header("การวิเคราะห์ความรู้สึกภาษาไทย")
st.subheader("Wiriya Hemmala | Data Science | NPRU")


col1, col2 = st.columns(2)
with col1:
    st.image('./pic/1.jpg')
    lot3="https://lottie.host/4b977781-5cbd-4197-8466-7c010f61a0f2/gIB4ii7vOk.json"
    lottie3 = load_lottieurl(lot3)
    st_lottie(lottie3)
with col2:
    st.image('./pic/DS1.jpg')
st.balloons()
