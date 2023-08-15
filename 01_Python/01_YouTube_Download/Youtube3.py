import os
import ssl
from pytube import YouTube
from pytube.cli import on_progress

# Disabling SSL certificate verification
#ssl._create_default_https_context = ssl._create_unverified_context

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    yt = YouTube(youtube_url, on_progress_callback=on_progress)

    try:
        print("Fetching video details...")
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1]
        print(f"Downloading video: {yt.title} | Resolution: {video_stream.resolution}")
        video_stream.download(output_path=destination_folder)
    except Exception as e:
        return f"ERROR | {e}"

    return f"Download Complete | Saved at {destination_folder}"

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=9c7Ti2OcLZg"
    dest = "./00_downloaded"
    result = download_highest_quality(url, dest)
    print(result)




