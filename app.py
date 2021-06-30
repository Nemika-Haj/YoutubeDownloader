import eel, sys

from youtubeDL import downloadSong, downloadVideo

eel.init("web")

def close(a, b):
    if not debug:
        sys.exit()

debug=False

eel.start("templates/main.html", block=False, close_callback=close)

@eel.expose
def download(url, _type):
    print("Download request received.")
    if _type.lower() == "video":
        return downloadVideo(url)
    elif _type.lower() == "song":
        return downloadSong(url)

while True:
    eel.sleep(10)