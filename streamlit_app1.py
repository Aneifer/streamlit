import streamlit as st
import numpy as np
from typing import Any

# Title of the blog post
st.title("My Journey into Abstract Painting")

# Subtitle or introduction
st.subheader("You can do it too")

st.write("""
    Welcome to my exploration of the abstract, a journey that has transformed my perspective on art and expression.
""")


image_url = "https://static.westwingnow.de/image/upload/c_limit/w_1500,h_2000/v1/simple/65/6381/2230052.jpg"
st.image(image_url, caption='Emotions can be pictured best by colours')

# Section headers and content, simulating blog post segments
st.header("The Beginning")
st.write("""
    My art started with capturing the world around me in great detail, from serene beaches to rolling hills. 
    Nature was my muse, and my canvas was a window to its soul.
""")

st.header("A Pivotal Moment")
st.write("""
    The real turning point came during a visit to a contemporary art museum. A single abstract painting caught my eye, 
    sparking an emotional and artistic awakening. It was as if the painting spoke directly to me, urging me to look beyond 
    the tangible and explore the emotions and ideas that lay beneath.
""")

st.header("Embracing Abstraction")
st.write("""
    Embracing abstraction meant letting go of precise details and diving into a world of colors, forms, and emotions. 
    My studio turned into a playground of imagination, where each piece became a reflection of my inner experiences 
    and a dialogue with the viewer.
""")

st.header("The Joy of Discovery")
st.write("""
    This journey has been about more than just changing my artistic style; it's been a profound journey of self-discovery. 
    Abstract art has allowed me to express the inexpressible, to communicate emotions and ideas that defy conventional representation.
""")

st.header("Sharing My Journey")
st.write("""
    Through this blog, I hope to share the insights, challenges, and joys of my journey into abstract painting. 
    Whether you're an artist or simply someone who appreciates art, I invite you to explore the beauty and depth of abstraction with me.
""")

st.write("Thank you for joining me on this journey. Let's continue to explore the boundless possibilities of abstract art together.")



link = 'https://www.thalia.de/shop/home/artikeldetails/A1057023285?ProvID=11000533&gad_source=1&gclid=CjwKCAiAuNGuBhAkEiwAGId4alH1Rv6F0m-2PFyHVFrUxw1SZQ-F67GWS4lOaI9pT7EungmNoWoSmBoCYhkQAvD_BwE'
st.markdown(f'<a href="{link}" target="_blank"><button style="color: white; background-color: #4CAF50; border: none; padding: 10px 24px; cursor: pointer;">Buy this book</button></a>', unsafe_allow_html=True)


video_url = "https://www.youtube.com/watch?v=H8EIrUBxgzw"
st.video(video_url)

# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

# Non-interactive elements return a placeholder to their location
# in the app. Here we're storing progress_bar to update it later.
progress_bar = st.sidebar.progress(0)

# These two elements will be filled in later, so we create a placeholder
# for them using st.empty()
frame_text = st.sidebar.empty()
image = st.empty()

m, n, s = 960, 640, 400
x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
    # Here were setting value for these two elements.
    progress_bar.progress(frame_num)
    frame_text.text("Frame %i/100" % (frame_num + 1))

    # Performing some fractal wizardry.
    c = separation * np.exp(1j * a)
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    C = np.full((n, m), c)
    M: Any = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))

    for i in range(iterations):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = i

    # Update the image placeholder by calling the image() function on it.
    image.image(1.0 - (N / N.max()), use_column_width=True)

# We clear elements by calling empty on them.
progress_bar.empty()
frame_text.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")