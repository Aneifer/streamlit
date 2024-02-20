# load libraries
import streamlit as st
from streamlit_lottie import st_lottie
import seaborn as sns
import pandas as pd
import requests
import altair as alt

# header
st.title("Palmer Penguins :pinguin:")
# subtitle
st.write("This is a simple example of a Streamlit app using the Palmer Penguins dataset")
# text
st.write("The Palmer Penguins dataset is a popular dataset for data exploration and visualization. The dataset contains various measurements of penguins, including bill length, bill depth, flipper length, body mass, and species.")
# text
st.write("In this example, we will use the Palmer Penguins dataset to create a simple Streamlit app that includes a bar chart, scatter plot, and a YouTube video.")
# animated penguin
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_penguin = load_lottieurl(
    "https://lottie.host/61d21d73-ab4b-43de-a5c0-5e67b0cdbd11/E87nM5RrTf.json"
)
st_lottie(lottie_penguin, height=500)
# title for dataset
st.title("Penguins dataset")
# import palmer penguins dataset
penguins = sns.load_dataset("penguins")
st.write(penguins)
# title for pandas
st.title("Bar chart with pandas")
# visualise the dataset
st.bar_chart(penguins["species"].value_counts())
# title for seaborn
st.title("Scatter plot with seaborn")
# plot a scatter plot
st.pyplot(sns.pairplot(penguins, hue="species"))
# title for altair
st.title("Scatter plot with altair")

# plot with altair with x-axis from 160 to 240 and y-axis from 12 to 22
chart = alt.Chart(penguins).mark_point().encode(
    x=alt.X('flipper_length_mm', scale=alt.Scale(domain=(160, 240))),
    y=alt.Y('bill_depth_mm', scale=alt.Scale(domain=(12, 22))),
    color='species'
)
st.altair_chart(chart, use_container_width=True)
# title for plotly
st.title("Scatter plot with plotly")

# plot with plotly
import plotly.express as px
fig = px.scatter(penguins, x="flipper_length_mm", y="bill_depth_mm", color="species")
st.plotly_chart(fig)
# title for youtube
st.title("Youtube video")
# youtube video
st.write("Youtube video")
# embed a youtube video
st.video("https://youtu.be/q3uXXh1sHcI")