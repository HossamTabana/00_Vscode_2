import os
import ssl
from pytube import YouTube
from pytube.cli import on_progress

# Disabling SSL certificate verification
#ssl._create_default_https_context = ssl._create_unverified_context

YouTube('https://youtu.be/9c7Ti2OcLZg').streams.first().download()

