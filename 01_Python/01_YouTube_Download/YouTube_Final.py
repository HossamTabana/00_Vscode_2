import os
import ssl
from pytube import YouTube
from pytube.cli import on_progress

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    yt = YouTube(youtube_url, on_progress_callback=on_progress)

    try:
        print("Fetching video details...")
        video_stream = sorted(yt.streams.filter(progressive=True, file_extension='mp4'), key=lambda s: s.resolution, reverse=True)[0]
        print(f"Downloading video: {yt.title} | Resolution: {video_stream.resolution}")
        video_stream.download(output_path=destination_folder)
    except Exception as e:
        return f"ERROR | {e}"

    return f"Download Complete | Saved at {destination_folder}"

if __name__ == "__main__":
    url = "https://youtu.be/At5alroIsic"
    dest = "./00_downloaded"
    result = download_highest_quality(url, dest)
    print(result)












