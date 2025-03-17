import streamlit as st  # Importing Streamlit library
import pandas as pd  # For handling data (optional)
import numpy as np  # For random number generation (optional)

# 🏆 Set up the page title and icon
st.set_page_config(page_title="Streamlit Widgets Demo", page_icon="✨", layout="centered")

# 🎨 Custom CSS for better UI styling
st.markdown("""
    <style>
        .stTextInput, .stSlider, .stButton {
            font-size: 16px;
            padding: 10px;
        }
        .stMarkdown {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
        .title {
            color: #ff6347;
            text-align: center;
            font-size: 30px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 App Title with Emoji
st.markdown('<p class="title">🚀 Interactive Widgets with Streamlit</p>', unsafe_allow_html=True)

# 📝 Text Input: Get the User's Name
name = st.text_input("🔤 Enter your name:", placeholder="Type your name here...")

# 🎚️ Slider: Select Age
age = st.slider("🎂 Choose your age:", min_value=1, max_value=100, value=25)

# 📌 Number Input: Enter any number
number = st.number_input("🔢 Enter a number:", min_value=0, max_value=100, value=10)

# 📅 Date Input: Select a Date
date = st.date_input("📅 Select a date:")

# 🎨 Color Picker: Choose a Color
color = st.color_picker("🎨 Pick a color:", "#00f900")

# 🖱️ Button: Click to Display a Message
if st.button("🚀 Submit"):
    st.success(f"Hello, {name}! You are {age} years old.")
    st.write(f"Your favorite color is {color} and you chose the number {number}.")
    st.write(f"You selected the date: {date}")

# 📊 Expander: Additional Info
with st.expander("📌 Learn More about Streamlit Widgets"):
    st.write("""
    - `st.text_input()` → Accepts user text input.
    - `st.slider()` → Allows selection within a range.
    - `st.number_input()` → Enables number input.
    - `st.date_input()` → Lets users pick a date.
    - `st.color_picker()` → Select a color.
    - `st.button()` → Click action trigger.
    - `st.expander()` → Displays additional information on demand.
    """)

# 🚀 Run the app using:
# 👉 `streamlit run app.py`
