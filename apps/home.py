# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests





def app():
    st.title('Home')
    st.markdown("""
                ## Drug Discovery App Using Lipinski's Rule-of-Five.
                



---
""")

    st.write('')

    st.write('**Welcome to the Drug Discovery App**')
   # st.image('3.png', width=800)
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    # "https://assets1.lottiefiles.com/packages/lf20_z3wd7moi.json"
    #def load_lottiefile(filepath: str):
        #with open(filepath, "r") as f:
            #return json.load(f)
    #lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_t7ok1nhk.json"
    lottie_json = load_lottieurl(lottie_url)

    st_lottie(
    lottie_json,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)
  
