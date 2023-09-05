import os
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    yt = YouTube(youtube_url, on_progress_callback=on_progress)
    print("Fetching video details...")
    
    # Fetch the video-only and audio-only streams.
    video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by("resolution").desc().first()
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Downloading video stream: {video_stream.resolution}")
    video_filename = video_stream.download(output_path=destination_folder, filename="video_temp")
    audio_filename = audio_stream.download(output_path=destination_folder, filename="audio_temp")
    
    # Combining video and audio using moviepy
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    
    final_filename = os.path.join(destination_folder, yt.title.replace("/", "-") + ".mp4")
    final_clip.write_videofile(final_filename)
    
    # Remove temporary files
    os.remove(video_filename)
    os.remove(audio_filename)

    return f"Download Complete | Saved at {final_filename}"

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dCRofZ1Ux_k"
    dest = "./00_VSCODE_2/01_Python/01_YouTube_Download/00_downloaded"
    result = download_highest_quality(url, dest)
    print(result)








