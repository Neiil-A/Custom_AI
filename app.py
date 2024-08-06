import streamlit as st

# Streamlit UI for inputting API keys
def get_api_keys():
    st.title("API Configuration")
    serperdev_api_key = st.text_input("Serperdev API Key", type="password")
    chatgpt_api_key = st.text_input("ChatGPT API Key", type="password")
    return serperdev_api_key, chatgpt_api_key

if __name__ == "__main__":
    serperdev_api_key, chatgpt_api_key = get_api_keys()
    st.write(f"Serperdev API Key: {serperdev_api_key}")
    st.write(f"ChatGPT API Key: {chatgpt_api_key}")
