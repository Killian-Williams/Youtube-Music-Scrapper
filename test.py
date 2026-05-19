from yt_dlp import YoutubeDL

# Playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PLr-GphmRp-izgrsEPJ2LHMTh14oe3-nNF'

# Set up options for yt-dlp
ydl_opts = {
    'outtmpl': 'C:\\Users\\Willi\\OneDrive\\Desktop\\hell\\%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4'
}

# Download the playlist
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Download complete!")
