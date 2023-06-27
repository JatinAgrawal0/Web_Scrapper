import BeautifulSoup
import requests
import logging
import time

def scrape_text(url, element_type, custom_tags=None):
    # Set headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Delay a few seconds to emulate human behavior
    time.sleep(2)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Check to make sure that `element_type` is a valid value
    if element_type not in ["Paragraphs", "Titles", "Paragraphs and Titles", "All", "Custom"]:
        raise ValueError("Invalid element_type")

    # Define all possible HTML elements
    all_elements = [
        "p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "span", "div",
        "a", "strong", "em", "blockquote", "pre", "code", "img", "table",
        "tr", "th", "td", "ul", "ol", "dl", "dt", "dd"
    ]

    if element_type == "Custom" and custom_tags:
        text_elements = soup.find_all(custom_tags)
    elif element_type == "Paragraphs":
        text_elements = soup.find_all("p")
    elif element_type == "Titles":
        text_elements = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    elif element_type == "Paragraphs and Titles":
        text_elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])
    else:
        text_elements = soup.find_all(all_elements)

    # Extract the text from the elements
    extracted_text = [element.get_text() for element in text_elements]

    # Log the progress of the scraping
    logging.info("Extracted %d text elements", len(extracted_text))

    return extracted_text
