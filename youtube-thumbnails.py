import os
from pytube import YouTube
import urllib.request
import sys

def download_thumbnail(url, output_dir="thumbnails"):
    os.makedirs(output_dir, exist_ok=True)
    
    video = YouTube(url)
    thumbnail_url = video.thumbnail_url
    
    video_id = video.video_id
    output_path = os.path.join(output_dir, f"{video_id}.jpeg") 
    
    
    urllib.request.urlretrieve(thumbnail_url, output_path)
    return output_path

def main():
    """Main function to run the script."""
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL as an argument")
        print("Usage: python youtube-thumbnails.py <youtube_url>")
        return
    
    url = sys.argv[1]
    result = download_thumbnail(url)
    print(result)

if __name__ == "__main__":
    main()