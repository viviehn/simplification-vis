import streamlit as st

st.set_page_config(layout='wide')

with open('models.txt') as f:
    models = f.read().splitlines()

exps = [5,35,65]


st.text('Each row shows a different model and scale [5,35,65].')
st.text('The first image is the original drawing, and the final drawing is the final image in the simplification sequence, i.e. if every possible simplification according to region constraints is made.')
st.text('The middle image shows an "automatically selected" image based on the combined loss function (LPIPS+Density -- see loss curves in view_plots).')
st.text('The index is computed as follows:')
st.text('Suppose we have a sequence of loss values, L. Find the location where L(t+1) - L(t) > threshold')
st.text('threshold is set to max(L)*.0005*scale')
cols = st.columns(3)
for m_name in models:
    for exp in exps:
        try:
            cols[0].image(f'autoselect/{m_name}_{exp}_orig.png')
            cols[1].image(f'autoselect/{m_name}_{exp}_select.png')
            cols[2].image(f'autoselect/{m_name}_{exp}_final.png')
        except:
            continue
