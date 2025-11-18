import streamlit as st

# Title
st.title("My Dummy Streamlit App")

# Sidebar
st.sidebar.header("Options")
name = st.sidebar.text_input("Enter your name:", "Guest")
show_message = st.sidebar.checkbox("Show welcome message")

# Main content
st.write("## Welcome to the Demo App")
st.write("This is a simple placeholder Streamlit application.")

# Button example
if st.button("Click me"):
    st.success("Button clicked!")

# Conditional message
if show_message:
    st.info(f"Hello, **{name}**! Thanks for visiting this dummy app.")

# Slider example
value = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {value}")

# Data table example
import pandas as pd
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})
st.write("### Sample Data")
st.table(df)
