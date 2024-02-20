import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# Title of the app
st.title("Penguin Data Visualization")

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Upload your penguin CSV file", type="csv")

# Check if there is a file uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write(df)

    # Scatter Plot with Matplotlib / Pyplot
    st.subheader("Scatter Plot with Pyplot")
    x_axis_pyplot = st.selectbox("Pyplot - Choose X axis", options=df.columns, index=df.columns.get_loc("bill_length_mm"))
    y_axis_pyplot = st.selectbox("Pyplot - Choose Y axis", options=df.columns, index=df.columns.get_loc("bill_depth_mm"))
    color_var_pyplot = st.selectbox("Pyplot - Choose Color Variable", options=df.columns, index=df.columns.get_loc("species"))

    fig, ax = plt.subplots()
    for species, d in df.groupby(color_var_pyplot):
        ax.scatter(d[x_axis_pyplot], d[y_axis_pyplot], label=species)
    ax.set_xlabel(x_axis_pyplot)
    ax.set_ylabel(y_axis_pyplot)
    ax.legend(title=color_var_pyplot)
    st.pyplot(fig)

    # Advanced Scatter Plot with Altair
    st.subheader("Interactive Scatter Plot with Altair")
    x_axis_altair = st.selectbox("Altair - Choose X axis", options=df.columns, index=df.columns.get_loc("flipper_length_mm"), key='x_altair')
    y_axis_altair = st.selectbox("Altair - Choose Y axis", options=df.columns, index=df.columns.get_loc("body_mass_g"), key='y_altair')
    color_var_altair = st.selectbox("Altair - Choose Color Variable", options=df.columns, index=df.columns.get_loc("species"), key='color_altair')

    # Creating an Altair chart
    scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis_altair,
        y=y_axis_altair,
        color=color_var_altair,
        tooltip=list(df.columns)
    ).interactive()

    # Display the Altair chart
    st.altair_chart(scatter_chart, use_container_width=True)

else:
    st.info("Please upload a CSV file to start.")
