# Install pytube first
# pip install pytube

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
from pytube import YouTube

def download_highest_quality(youtube_url, destination_folder):
    # Ensure the folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Fetch video details
    yt = YouTube(youtube_url)
    
    # Filter out only the video streams and sort them by resolution and select the highest resolution
    video_stream = sorted(yt.streams.filter(progressive=True, file_extension='mp4'), key=lambda s: s.resolution, reverse=True)[0]
    #video_stream = sorted(yt.streams.filter(progressive=True, file_extension='mp4'), key=lambda s: s.resolution, reverse=True)[0]
    
    #video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1]

    
    # Print download started status
    print(f"Starting download for {yt.title} in {video_stream.resolution} resolution...")
    
    # Download the video
    video_stream.download(output_path=destination_folder)
    
    # Print download completed status
    print(f"Download completed! Saved in {destination_folder}")

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=9c7Ti2OcLZg"
    dest = "./00_downloaded"
    download_highest_quality(url, dest)









