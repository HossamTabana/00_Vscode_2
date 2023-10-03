import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
import ssl
from pytube import YouTube

# Disabling SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
  #def download_yt_video(inp_command):
   # ytURL = input("Enter the URL of the YouTube video: ")
    yt = YouTube(youtube_url)
    try:
        print("Downloading...")
        yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1].download(output_path=destination_folder)
    except:
        return "ERROR | Please try again later"
    return f"Download Complete | Saved at {os.getcwd()}"

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=9c7Ti2OcLZg"
    dest = "./00_downloaded"
    download_highest_quality(url, dest)




