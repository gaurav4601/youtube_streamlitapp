import streamlit as st
from pytube import YouTube
from PIL import Image
import time

url = "https://cdn.mos.cms.futurecdn.net/8gzcr6RpGStvZFA2qRt4v6.jpg"
text = "YouTube Video Downloader"
span_html = f"<span><img src='{url}' width='100px' style='margin-right: 10px'></span>"
    
# Display the image and text as span
st.markdown(span_html, unsafe_allow_html=True)

st.title("YouTube Video Downloader")

# Get the YouTube video URL from the user
url = st.text_input("Enter the YouTube video URL:")
if st.button("Download"):
    st.write("Downloading Started")
    if url:
        try:
            # Create a YouTube object
            yt = YouTube(url)

            # Get the video title and author
            title = yt.title
            author = yt.author

            # Get the highest quality video stream
            stream = yt.streams.get_highest_resolution()

            # Download the video
            st.write(f"Downloading video '{title}'")
            stream.download()
            progress_slot = st.empty()
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
                progress_slot.text(f"Downloading file ({i + 1}%)")
            progress_slot.text("Download complete")
            st.video(title + '.mp4')

        except Exception as e:
            st.write(f"Error: {e}")


       
