import streamlit as st
import glob
import os
import itertools
import pickle
import numpy as np
import pydiffvg, torch
import utils

st.set_page_config(layout='wide')

cols = st.columns(6)
rows = 101

for r in range(rows):
    for c in range(6):
        cols[c].image(f'view_sequence_row/{r}_{c}.png')
