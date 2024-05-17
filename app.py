import streamlit as st
import requests
from datetime import date
from bs4 import BeautifulSoup
import urllib

# Constants
BASE_URL = 'https://apod.nasa.gov/apod/'
API_KEY = 'yd3rfzu7WelJMyVFNI5sM1fYpVnYIfTRKuSHIfOI'

def fetch_apod_data(selected_date):
    date_str = selected_date.strftime('%y%m%d')
    url = f'{BASE_URL}ap{date_str}.html'
    response = requests.get(url)
    if response.status_code != 200:
        st.error('Failed to retrieve data for the selected date. Response code: {}'.format(response.status_code))
        return None
    return response.text

def parse_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    # Initialization
    title = media_url = media_type = explanation = None

    # Title
    try:
        title = soup.find('b').text.strip()
    except AttributeError:
        st.error('Failed to extract title.')

    # Media type and URL
    img_tag = soup.find('img')
    if img_tag:
        media_type = 'image'
        media_url = BASE_URL + img_tag['src']
    else:
        iframe_tag = soup.find('iframe')
        if iframe_tag:
            media_type = 'video'
            media_url = iframe_tag['src']

    # Explanation
    paragraphs = soup.findAll('p')
    for p in paragraphs:
        if "Explanation:" in p.text:
            explanation = p.text.split("Explanation:")[1].strip().split("Tomorrow's picture:")[0].strip()

    return {
        'title': title,
        'media_url': media_url,
        'media_type': media_type,
        'explanation': explanation
    }

def display_apod(apod_data):
    st.title(apod_data['title'])
    if apod_data['media_type'] == 'image':
        st.image(apod_data['media_url'])
    elif apod_data['media_type'] == 'video':
        st.video(apod_data['media_url'])

    st.write(apod_data['explanation'])

def main():
    # Set space background
    st.markdown(
        """
        <style>
        body {
            background-image: url("https://wallpaperaccess.com/full/2180284.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Customize theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgba(0,0,0,0.6);
            color: white;
        }
        .stTextInput > div > div > input {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("NASA Picture of the Day")
    selected_date = st.date_input("Select a Date", value=date.today(), min_value=date(1995, 6, 16), max_value=date.today())

    if st.button("And the picture of the day is..."):
        html_data = fetch_apod_data(selected_date)
        if html_data:
            apod_data = parse_data(html_data)
            display_apod(apod_data)

            # Option to download the image
            if apod_data['media_type'] == 'image':
                download_link = f"[Download Image]({apod_data['media_url']})"
                st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
