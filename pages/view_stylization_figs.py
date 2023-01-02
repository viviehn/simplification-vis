import streamlit as st
import glob as glob

st.set_page_config(layout='wide')

files = glob.glob('stylization_figs/*.png')

for f in files:
    st.image(f)
