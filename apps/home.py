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
    st.image('12.png', width=800)
  
