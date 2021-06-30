import youtube_dl, os

song_settings = {
    "outtmpl": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'Youtube Downloader', '%(title)s.%(ext)s'),
    "format": "bestaudio/best",
    "noplaylist": True,
    "no_warnings": True,
    "ignoreerrors": True,
    "quiet": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "logtostder": False,
    "nocheckcertificate": True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

video_settings = {
    "outtmpl": os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'Youtube Downloader', '%(title)s.%(ext)s'),
    "format": "best",
    "noplaylist": True,
    "no_warnings": True,
    "ignoreerrors": True,
    "quiet": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "logtostder": False,
    "nocheckcertificate": True
}

song_source = youtube_dl.YoutubeDL(song_settings)
video_source = youtube_dl.YoutubeDL(video_settings)

def downloadSong(url):
    song = song_source.extract_info(url)

    if song: return 1

    return 0

def downloadVideo(url):
    video = video_source.extract_info(url)

    if video: return 1

    return 0