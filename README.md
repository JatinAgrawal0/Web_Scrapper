# Web Scrapper

🌐 Web Text Scraper is your go-to tool for effortlessly extracting text elements from web pages. 🧰 Customize your extraction process by selecting 📃 paragraphs, 🏷️ titles, or specific HTML tags. With robust error handling and a visually appealing display of the extracted text, it simplifies web scraping, making data gathering a breeze. 🚀

## 🔧 Features:
-Flexible Element Selection: Choose the type of elements to scrape, such as paragraphs, titles, or custom HTML tags. 🖋️
-Interactive Interface: User-friendly interface for entering the URL and selecting scraping options. 🌐
-Real-Time Text Extraction: Extract text from the provided URL in real-time upon clicking the "Scrape" button. ⏳
-Feedback Messages: Display messages indicating success, warnings, or errors during the scraping process. 📢



## 📥 Installation:

To run the Web Text Scraper, make sure you have the following dependencies installed:

- streamlit
- beautifulsoup4==4.11.1
- pip==23.1.2
- requests==2.28.0

You can install these dependencies by running the following command:

👉 pip install -r requirements.txt 👈


## 📝 Usage:

1. Run the streamlit_app.py script using the following command:

🚀 python streamlit_app.py 🚀
2. The Streamlit application will launch in your browser.

3. Enter the URL of the web page you want to scrape in the provided text input. 🌐

4. Select the type of elements you want to scrape from the available options: "Paragraphs", "Titles", "Paragraphs and Titles", "All", or "Custom". 📑

5. If you choose the "Custom" option, you can enable the "Custom Tag" checkbox and enter the HTML tags you want to extract, separated by commas. 💻

6. Click the "Scrape" button to initiate the scraping process. 🕷️

7. If the scraping is successful, the extracted text will be displayed on the page. 📄

8. If no text elements are found, a warning message will be shown. ⚠️

9. In case of any errors during the scraping process, an error message will be displayed. ❌
### 📌 Note:

Make sure to replace 'Jatin_Agrawal_20BCS6606' with your desired page title and 'LOGO.png' with the path to your desired page icon in the set_page_config function.

## Contributing 🤝

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE).

   


