import streamlit as st
from streamlit.components.v1 import components

st.set_page_config(layout="wide")
# PHP file URL
# Get the URL of the PHP file
php_url = "http://sigj.atwebpages.com/doc/index.php"

# Embed the PHP file using an iframe
st.components.v1.iframe(php_url, height=1000)

# Example usage with optional parameters
# components.iframe(src=php_file_url, width=1000, height=600)
