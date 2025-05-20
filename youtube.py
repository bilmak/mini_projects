import yt_dlp  # yt_dlp is a modern alternative to youtube-dl
import sys

if len(sys.argv) < 2:
    print("Input your URL")
    sys.exit(1)

url = sys.argv[1]

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'  # specifies a filename pattern
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    print(f"Title: {info['title']}")
    ydl.download([url])
