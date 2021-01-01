from __future__ import unicode_literals
import os
import youtube_dl

URL = input('Put url here > ')
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    if d['status'] == 'downloading':
        print(d['filename'],'-', d['_percent_str'])
    #global file__name
    #file__name = d['filename']
    #file__name = file__name[:-4]


ydl_opts = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'outtmpl': 'downloaded-songs/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
    {'key': 'EmbedThumbnail'},
    {'key': 'FFmpegMetadata'}],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])

question = input("Do you wish to open the file? (Y/N)\n> ")
if question.lower() == "y" or question.lower() == "yes":
    file__name = f"{file__name}mp3"
    os.startfile(file__name)
    exit()
else:
    exit()