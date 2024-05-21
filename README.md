# NASA Picture of the Day App

This Streamlit application allows users to view the NASA Astronomy Picture of the Day (APOD) for a selected date. The user can select any date from June 16, 1995, to the current date, and the application fetches and displays the corresponding APOD, including the title, media (image or video), and explanation.

## Features

- Fetch APOD data for a selected date
- Display the APOD image or video along with its title and explanation
- Allow users to download the APOD image
- Custom background and theme for an enhanced user experience

## Prerequisites

To run this application, you need to have the following installed:

- Python 3.6 or higher
- Streamlit
- Requests
- BeautifulSoup4

## Notes
Ensure you have an active internet connection as the application fetches data from the NASA APOD website.
The APOD API Key (API_KEY) is mentioned in the constants section but not used in the current code. If you have an API key from NASA, you can modify the code to use the APOD API for fetching data instead of web scraping.

## Customization
The background and theme can be customized by modifying the CSS in the st.markdown sections of the main function.
Additional features can be added, such as displaying more metadata, adding more download options, or supporting different media formats.

## License
This project is open source and available under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements
NASA APOD: https://apod.nasa.gov/apod/astropix.html
Streamlit: https://streamlit.io/
BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
