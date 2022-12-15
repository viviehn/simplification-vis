import streamlit as st

st.set_page_config(layout='wide')

with open('models.txt') as f:
    models = f.read().splitlines()

exps = [5,35,65]

cols = st.columns(3)
for m_name in models:
    for exp in exps:
        try:
            cols[0].image(f'autoselect/{m_name}_{exp}_orig.png')
            cols[1].image(f'autoselect/{m_name}_{exp}_select.png')
            cols[2].image(f'autoselect/{m_name}_{exp}_final.png')
