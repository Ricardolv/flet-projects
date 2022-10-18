from pytube import YouTube
from sys import argv


v  = argv[1]
yt = YouTube("https://youtu.be/" + v)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download()

