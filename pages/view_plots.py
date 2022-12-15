import streamlit as st

st.set_page_config(layout='wide')

with open('models.txt') as f:
    models = f.read().splitlines()

st.text('Plots per model of the summed loss function (LPIPS+Density).')
st.text('Note that there is some pre-processing of each line drawing before the algorithm is run. This pre-processing depends on the scale parameter, so index=0 of each curve does not correspond to the exact same drawing.')
for m_name in models:
    try:
        st.image(f'plots/{m_name}.png')
    except:
        continue
