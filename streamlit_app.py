import streamlit as st
from web_scraper import scrape_text

st.set_page_config(page_title='Jatin_Agrawal_20BCS6606', page_icon = 'LOGO.png', initial_sidebar_state = 'auto')

st.title("Web Text Scraper")

url = st.text_input("Enter the URL to scrape:", "")
element_type = st.selectbox("Select the type of elements to scrape:", ["Paragraphs", "Titles", "Paragraphs and Titles", "All", "Custom"])
custom_tags = None

if element_type == "Custom":
    use_custom_tag = st.checkbox("Custom Tag")
    if use_custom_tag:
        custom_tags = st.text_input("Enter the HTML tags to extract (comma-separated):")
        custom_tags = [tag.strip() for tag in custom_tags.split(",")]

if st.button("Scrape"):
    if url:
        try:
            extracted_text = scrape_text(url, element_type, custom_tags)
            if extracted_text:
                st.success("Text extraction successful!")
                st.write(extracted_text)
            else:
                st.warning("No text elements found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid URL.")
