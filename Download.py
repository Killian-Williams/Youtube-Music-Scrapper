from googleapiclient.discovery import build
from pytube import YouTube

api_key = "AIzaSyC-va4e-2BfSm6ifLu-1oo0Te2HSdy5Jeg"
youtube = build('youtube', 'v3', developerKey=api_key)

# Get playlist items
request = youtube.playlistItems().list(
    part='contentDetails',
    playlistId='PLr-GphmRp-izgrsEPJ2LHMTh14oe3-nNF',
    maxResults=50  # Adjust as needed
)
response = request.execute()

# Extract video IDs
video_ids = [item['contentDetails']['videoId'] for item in response['items']]

# Base URL for YouTube videos
base_url = 'https://www.youtube.com/watch?v='

# Download each video
for video_id in video_ids:
    video_url = f'{base_url}{video_id}'
    yt = YouTube(video_url)
    print(f'Downloading: {yt.title}')
    yt.streams.filter(progressive=True, file_extension='mp4').first().download(output_path='C:\\Users\\Willi\\OneDrive\\Desktop\\hell')
    print(f'Downloaded: {yt.title}')

print("All videos downloaded.")
