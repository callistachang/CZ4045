from src.utils import load_data_pandas
import streamlit as st
from .utils import load_data_pandas
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling


def build_piechart(df):
    fig, ax = plt.subplots()
    values = df["stars"].value_counts()
    ax.set_title("Stars in Reviews")
    ax.pie(
        values.to_list(),
        labels=values.keys().to_list(),
        autopct="%1.1f%%",
        startangle=90,
    )
    st.pyplot(fig)


def build_boxplot(df, col_name):
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=df[col_name].where(lambda x: x <= 85),
            name=col_name.capitalize(),
        )
    )
    fig.update_layout(
        yaxis=dict(
            title="Number of reviews",
            showgrid=True,
        ),
        height=400,
        xaxis=dict(title=f"Number of users who found the review {col_name}"),
        title=dict(text=f"Reviews Labelled {col_name.capitalize()}"),
    )
    st.plotly_chart(fig)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def generate_report(df):
    return df.profile_report()


def app():
    filepath = "src/reviewSelected100.json"
    df = load_data_pandas(filepath)
    st.markdown(
        f"""
# Dataset Analysis

The dataset we are analyzing is `reviewSelected100.json`.

---

## Basic Statistics 

**Total number of reviews in dataset:** {len(df)}

**Total number of unique users in dataset:** {df['user_id'].nunique()}

**Total number of unique businesses in dataset:** {df['business_id'].nunique()}

---

## Number of Stars

Most reviews are 5-star reviews, followed by 4-star reviews and 1-star reviews.
"""
    )
    build_piechart(df)
    st.markdown(
        """
---

## Useful, Funny and Cool Reviews

Most reviews have only 0-2 other users who found it useful, funny or cool. 
However, there are some reviews with more than 50 labels. This is likely because 
reviews in Yelp are sorted by popularity and helpfulness, causing other reviews to 
get 'buried' in the crowd.
    """
    )
    build_boxplot(df, "useful")
    build_boxplot(df, "funny")
    build_boxplot(df, "cool")
    st.markdown(
        """
---

## Overall Profile Report of Dataset
    """
    )
    st_profile_report(generate_report(df))
