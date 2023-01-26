# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:34:11 2023

@author: j.videlefsky
"""

"""
Creating Virtual Environment:
conda create -n stenv python=3.9
conda env list
conda activate stenv
"""

# pip install streamlit
# streamlit hello

import streamlit as st

st.write('Hello Jared!')

st.header('st.button')

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')