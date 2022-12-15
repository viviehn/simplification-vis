import streamlit as st

st.set_page_config(layout='wide')

cols = st.columns(6)
rows = 113

for r in range(rows):
    for c in range(6):
        cols[c].image(f'view_sequence_row/{r}_{c}.png')
