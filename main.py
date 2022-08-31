import streamlit as st 
import requests as rq
import pandas as pd
import numpy as np
import time
from get_whitewhale_data import fetch

header = st.container()
dataset = st.container()

data_load_state = st.text('Loading data...')
data = fetch()
data_load_state.text("Done!")

with header: 
    st.title("Cosmos Validator Analysis")
    # v_data = pd.DataFrame(data)
    st.header("Income:")
    st.write(data)
