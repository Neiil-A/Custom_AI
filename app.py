# app.py
import streamlit as st
from streamlit_auth0 import login_button

# Streamlit UI for inputting API keys
st.title("GitHub OAuth Configuration")
client_id = st.text_input("GitHub Client ID")
client_secret = st.text_input("GitHub Client Secret", type="password")
auth0_domain = st.text_input("Auth0 Domain")
callback_url = st.text_input("Callback URL")

if st.button("Save and Authenticate"):
    if client_id and client_secret and auth0_domain and callback_url:
        auth0_config = {
            'client_id': client_id,
            'client_secret': client_secret,
            'domain': auth0_domain,
            'redirect_uri': callback_url
        }
        login_info = login_button(auth0_config)
        if login_info:
            st.write(f"Welcome {login_info['name']}!")
        else:
            st.write("Please log in using your GitHub account.")
    else:
        st.warning("Please fill in all the fields.")
