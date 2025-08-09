import streamlit as st
import pandas as pd

def upload_csv():
    return st.file_uploader("Upload File", type=["csv"])
