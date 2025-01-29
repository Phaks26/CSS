#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:44:18 2025

@author: delisa
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("STREAMLIT IS COOL")
st.title("Hello world")
st.header("Sample Data")
data = pd.DataFrame({"x":[1, 2 ,3], "y":[10, 20,30]})
number  = st.slider("Pick a number", 1, 100)
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")
st.plotly_chart(fig)
st.write("This is my first web")