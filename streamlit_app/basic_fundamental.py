# 📌 Import necessary libraries
import streamlit as st  # Main library for creating Streamlit apps
import pandas as pd  # Used for handling tabular data
import numpy as np  # Used for numerical operations
import matplotlib.pyplot as plt  # For creating visualizations

# 🏆 Set up the Streamlit app configuration
st.set_page_config(page_title="Streamlit Fundamentals", page_icon="📌", layout="centered")

# 🎨 Custom CSS for better UI styling
st.markdown("""
    <style>
        .title {text-align: center; font-size: 32px; font-weight: bold; color: #FF6347;}
        .subheader {text-align: center; font-size: 20px; font-weight: bold; color: #4682B4;}
    </style>
""", unsafe_allow_html=True)

# 🚀 Title and Introduction
st.markdown('<p class="title">🚀 Streamlit Fundamentals Explained</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">An interactive guide to learning Streamlit</p>', unsafe_allow_html=True)

# 🔹 **1. Displaying Text in Streamlit**
st.header("📌 1. Displaying Text")

# 📌 Streamlit has different functions for displaying text:
st.text("This is simple text using st.text()")
st.markdown("**This is bold text using st.markdown()**")
st.write("This is text using st.write() which automatically formats output.")

# 🔹 **2. Taking User Input**
st.header("📝 2. User Input")

# 📌 Text input field
name = st.text_input("🔤 Enter your name:", placeholder="Type your name here...")

# 📌 Numeric input (Slider)
age = st.slider("🎂 Choose your age:", min_value=1, max_value=100, value=25)

# 📌 Number input box
salary = st.number_input("💰 Enter your salary:", min_value=1000, max_value=100000, value=50000, step=1000)

# 📌 Date Input
dob = st.date_input("📅 Select your date of birth:")

# 📌 Color Picker
fav_color = st.color_picker("🎨 Pick your favorite color:", "#00f900")

# 📌 Button to display user details
if st.button("✅ Submit"):
    st.success(f"Hello, {name}! You are {age} years old.")
    st.write(f"Your selected date of birth is {dob}. Your favorite color is {fav_color}.")
    st.write(f"You entered a salary of **${salary}**.")

# 🔹 **3. Uploading and Handling Files**
st.header("📂 3. File Upload")

# 📌 File uploader widget
uploaded_file = st.file_uploader("📤 Upload a CSV file:", type=["csv"])

# 📌 Display the uploaded file
if uploaded_file:
    df = pd.read_csv(uploaded_file)  # Read CSV file
    st.write("📊 **Preview of Uploaded Data:**")
    st.dataframe(df)  # Display the data as a table

# 🔹 **4. Creating Charts and Visualizations**
st.header("📊 4. Data Visualization")

# 📌 Generate random data for plotting
data = np.random.randn(100, 2)  # 100 rows, 2 columns

# 📌 Create a DataFrame for visualization
df_chart = pd.DataFrame(data, columns=["X Values", "Y Values"])

# 📌 Plot a line chart
st.line_chart(df_chart)

# 📌 Plot a bar chart
st.bar_chart(df_chart)

# 📌 Creating a Matplotlib Figure
fig, ax = plt.subplots()
ax.hist(data[:, 0], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)  # Display the histogram in Streamlit

# 🔹 **5. Conditional Display & Expander**
st.header("🎭 5. Conditional Elements")

# 📌 Checkbox Example
show_message = st.checkbox("🔘 Show a secret message")
if show_message:
    st.success("🎉 You unlocked the secret message!")

# 📌 Expander Example
with st.expander("📌 Click to expand for more information"):
    st.write("This is hidden content inside an expander!")

# 🔹 **6. Columns for Layout**
st.header("📐 6. Layout with Columns")

# 📌 Create two columns
col1, col2 = st.columns(2)

with col1:
    st.info("ℹ️ This is the left column!")

with col2:
    st.warning("⚠️ This is the right column!")

# 🔹 **7. Sidebar for Navigation**
st.sidebar.header("🧭 Navigation")
st.sidebar.text("Use the sidebar for navigation!")
st.sidebar.selectbox("🔗 Select a Page:", ["Home", "Dashboard", "Settings"])

# 🔹 **8. Running Python Functions in Streamlit**
st.header("⚙️ 8. Running Python Functions")

# 📌 Function to square a number
def square_number(num):
    return num ** 2

# 📌 User input for a number
num = st.number_input("🔢 Enter a number to square:", min_value=0, max_value=100, value=5)

# 📌 Display squared result
if st.button("🎯 Calculate Square"):
    st.success(f"The square of {num} is {square_number(num)}.")

# 🚀 **Final Message**
st.markdown("### 🎉 Congratulations! You've learned the basics of Streamlit! 🚀")

# 🎯 **How to Run This App?**
# - Save this script as `app.py`
# - Run in terminal: `streamlit run app.py`
