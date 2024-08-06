import requests
from markdownify import MarkdownConverter
from bs4 import BeautifulSoup

class ExtractionTools:
    @staticmethod
    def url_to_md(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        markdown_text = MarkdownConverter().convert_soup(soup)
        return markdown_text

    @staticmethod
    def extract_context_from_web(prompt):
        # Placeholder for extracting context from the web based on the prompt
        # This function should be implemented to scrape web content relevant to the prompt
        url = "https://example.com/context"  # Replace with logic to determine URL based on prompt
        return ExtractionTools.url_to_md(url)

    @staticmethod
    def generate_reference_db(prompt):
        # Placeholder for generating a reference database based on the prompt
        # This function should be implemented to create a reference database with text, images, etc.
        reference_db = "path/to/reference_db"  # Replace with logic to generate reference database
        return reference_db
