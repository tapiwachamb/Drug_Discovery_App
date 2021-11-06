# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os

from PIL import Image
from multiapp import MultiApp
from apps import home, eda # import your app modules here
img = Image.open("android-chrome-384x384.png")
app = MultiApp()

st.set_page_config(page_icon=img)
#st.image('unnamed.png', width=200)

st.sidebar.markdown("""# Drug Discovry App

""")
with st.sidebar.header(''):
    

    app.add_app("Home", home.app)
    app.add_app("Drug Discovery", eda.app)
 
   
    
   # app.add_app("Predictions", model.app)
    
    
    
    
st.markdown("""




""")
primaryColor = st.get_option("theme.primaryColor")
s = f"""
<style>
div.stButton > button:first-child {{ border: 10px solid {primaryColor};background-color: #6C63FF;color:white;font-size:16px;height:3em;width:18.5em; border-radius:5px 5px 5px 5px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)
# Add all your application here

# The main app
app.run()
