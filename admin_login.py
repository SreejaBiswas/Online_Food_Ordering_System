
import streamlit as st
import pandas as pd

from userdata import get_user_data 

def user_data_table():
    df = pd.DataFrame(get_user_data())
    return df