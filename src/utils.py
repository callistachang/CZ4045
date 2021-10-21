import pandas as pd
import spacy
import streamlit as st
import json


def load_data_pandas(filepath):
    with open(filepath, encoding="utf-8") as f:
        df = pd.read_json(f.read(), lines=True)
    return df


def load_data_json(filepath, review_text):
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if review_text == data["text"]:
                return data
    return None


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(model_name):
    nlp = spacy.load(model_name)
    return nlp
