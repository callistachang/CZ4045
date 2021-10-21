import streamlit as st
import pandas as pd
import spacy


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_data(filepath):
    with open(filepath) as f:
        df = pd.read_json(f.read(), lines=True)
    return df


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(model_name):
    nlp = spacy.load(model_name)
    return nlp
