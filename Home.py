import streamlit as st
import libs as glib
import json

# Set up the page configuration

st.title(":rainbow[AWS Stock Analysis Assistant]")

# Load CSS for styling
with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Title and description
# st.markdown("<h1 class='header'>Stock Analysis Assistant</h1>", unsafe_allow_html=True)
st.write(":rainbow[Welcome to the Stock Analysis Assistant. Enter your stock-related queries below and receive instant insights!]")

# Chat input
input_text = st.text_input(":rainbow[Enter your query here...]")
if input_text:
    try:
        # Call the custom library function to get a response
        response = glib.call_claude_sonet_stream(input_text)
        # Display the response
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try again later.")
