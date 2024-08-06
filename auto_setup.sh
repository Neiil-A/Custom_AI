#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment for a MAC OS, change if you use Windows 
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Load environment variables
export $(grep -v '^#' API.env | xargs)

export GITHUB_CLIENT_ID='your_client_id_here'
export GITHUB_CLIENT_SECRET='your_client_secret_here'
export GITHUB_AUTH0_DOMAIN='your_auth0_domain_here'
export GITHUB_CALLBACK_URL='your_callback_url_here'

# Run the app
streamlit run app.py
