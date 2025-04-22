Video Downloader Script

📌 Overview

This is a multi-platform video downloader built using Python and yt-dlp. It supports downloading videos from:

YouTube

Instagram

Twitter (X)

Facebook

TikTok (Planned)

The script automatically detects the platform and downloads the highest quality video, merging audio when necessary using FFmpeg.

🔧 Installation

1️⃣ Install Required Dependencies

pip install yt-dlp rich uvicorn

2️⃣ Install FFmpeg (Required for Best Quality)

Windows

Download FFmpeg from gyan.dev.

Extract it to C:\ffmpeg\.

Add C:\ffmpeg\bin to the system PATH.

Verify installation with:

ffmpeg -version

Linux (Ubuntu/Debian)

sudo apt update && sudo apt install ffmpeg -y

macOS

brew install ffmpeg

🚀 How to Use

1️⃣ Run the Script

python download_video.py

2️⃣ Paste the Video URL

Example:

🔗 Enter the video URL: https://www.youtube.com/watch?v=3JZ_D3ELwOQ

3️⃣ The video will be saved in the downloaded_videos/ folder.

🛠 Features

✅ Supports YouTube, Instagram, Twitter, Facebook✅ Uses yt-dlp for reliable downloads✅ Automatically detects platform✅ Merges audio and video (with FFmpeg)✅ Handles errors gracefully✅ Supports TikTok (Planned)

📂 File Structure

📂 VideoDownloader
 ├── download_video.py  # Main script
 ├── README.md          # Documentation
 ├── downloaded_videos/ # Downloaded files

⚠️ Notes

Some Instagram and Facebook videos require login (session cookies support to be added).

Twitter/X video links expire quickly, so download them immediately.


steps cmd(run as administrator)
cd C:\Users\Dell.com\Desktop\AI\download_video
python C:\Users\Dell.com\Desktop\AI\download_video\download_video.py
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
http://127.0.0.1:8000/docs#/
ctrl+c to exit

