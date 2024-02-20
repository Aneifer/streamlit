import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.io import to_image

# Sample dataset creation function
def create_sample_data():
    items = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E']
    categories = ['Category 1', 'Category 2', 'Category 1', 'Category 2', 'Category 1']
    prices = np.random.randint(10, 100, size=len(items))
    data = pd.DataFrame({'Item': items, 'Category': categories, 'Price': prices})
    return data

# Load or create your dataset
df = create_sample_data()

# Sidebar
st.sidebar.header('Filters & Options')
selected_category = st.sidebar.selectbox('Select a Category', df['Category'].unique())

# New: Sidebar option to choose between graph and video
content_type = st.sidebar.radio('Choose content type:', ('Graph', 'Video'))

# Main area
st.title('Dashboard with Dynamic Content')
st.write('This app demonstrates dynamic content display based on sidebar selection.')

# Filtering data based on sidebar selection
filtered_data = df[df['Category'] == selected_category]

# Using columns to layout the dashboard
col1, col2 = st.columns(2)

with col1:
    st.header('Filtered Data')
    st.dataframe(filtered_data)

with col2:
    st.header('Content Display')

    # Conditional display based on sidebar radio button selection
    if content_type == 'Graph':
        # Create a Plotly graph for the selected category
        fig = px.bar(filtered_data, x='Item', y='Price', title=f'Prices in {selected_category}')

        # Convert Plotly figure to PNG image bytes
        fig_image = to_image(fig, format='png')

        # Display the image in Streamlit
        st.image(fig_image, caption=f'Price Distribution in {selected_category}', use_column_width=True)

    elif content_type == 'Video':
        # Display a video (replace 'path_to_video.mp4' with your video file path or URL)
        st.video('https://www.youtube.com/watch?v=FekNbHJgYP0')

# Optionally, you can add more interactive elements or visualizations as needed
