import youtube_dl

def download_highest_quality(youtube_url, destination_folder):
    # Configuration for downloading the best quality
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': destination_folder + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # one of avi, flv, mkv, mp4, ogg, webm
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    url = "https://youtu.be/At5alroIsic"
    dest = "./00_downloaded"  # replace with your desired destination
    download_highest_quality(url, dest)

