import streamlit as st
import os

class ContentGeneratorUI:
    def generate_content(self, prompt, link, openai_key, serper_key, model):
        """
        Generates content based on the given prompt, link, and API keys.
        
        Args:
            prompt (str): The prompt for content generation.
            link (str): The link for contextual content.
            openai_key (str): OpenAI API key.
            serper_key (str): SerperDev API key.
            model (str): Model selection for content generation.

        Returns:
            str: Generated content.
        """
        # Set environment variables for API keys
        os.environ["OPENAI_API_KEY"] = openai_key
        os.environ["SERPER_API_KEY"] = serper_key

        # Set the model name based on the user selection
        model_name = "gpt-4o" if model == "gpt-4o (5-10 cents)" else "gpt-4o-mini"
        os.environ["OPENAI_MODEL_NAME"] = model_name

        # Placeholder for content generation logic
        # Implement your content generation logic here
        result = f"Generated content based on prompt: '{prompt}' and link: '{link}' using model: '{model_name}'"

        return result

    def content_generation(self):
        """
        Manages the content generation process and updates the Streamlit session state.
        """
        if st.session_state.generating:
            st.session_state.content = self.generate_content(
                st.session_state.prompt, st.session_state.link, st.session_state.openai, st.session_state.serper, st.session_state.model
            )
            st.write("Content generated successfully!")
            st.text_area("Generated Content", st.session_state.content)
            st.session_state.generating = False

    def sidebar(self):
        """
        Renders the sidebar with input fields for the user to provide necessary information.
        """
        with st.sidebar:
            st.title("Written Content Generator ✍️")

            st.write(
                """
                To get started, enter a prompt for the new content you would like to be generated, specifying type of content (blogpost, LinkedIn post, etc.), as well as any word count limitations or other details.
                Additionally, provide a URL to a writing piece you would like to be used for stylistic/formatting context.
                """
            )

            st.text_area("Prompt", key="prompt", placeholder="Write a blogpost about...")
            st.text_input("Link", key="link", placeholder="https://www.example.com/blog...")
            
            url_openai = "https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key"
            st.text_input("OpenAI API Key (click [here](%s) for more)" % url_openai, key="openai", type="password")

            url_serper = "https://serper.dev/api-key"
            st.text_input("SerperDev API Key (click [here](%s) for more)" % url_serper, key="serper", type="password")

            model_options = ["gpt-4o-mini (1-3 cents)", "gpt-4o (5-10 cents)"]
            st.selectbox("Select an OpenAI model", options=model_options, key="model")

            if st.button("Generate!"):
                st.session_state.generating = True

    def render(self):
        """
        Sets up the main layout of the Streamlit app.
        """
        st.set_page_config(page_title="Written Content Generator", page_icon="✍️")

        if "prompt" not in st.session_state:
            st.session_state.prompt = ""
        if "link" not in st.session_state:
            st.session_state.link = ""
        if "openai" not in st.session_state:
            st.session_state.openai = ""
        if "serper" not in st.session_state:
            st.session_state.serper = ""
        if "content" not in st.session_state:
            st.session_state.content = ""
        if "generating" not in st.session_state:
            st.session_state.generating = False

        self.sidebar()
        self.content_generation()

if __name__ == "__main__":
    ContentGeneratorUI().render()
