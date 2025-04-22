from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, HttpUrl
from fastapi.responses import FileResponse
from typing import List
import os
from download_video import VideoDownloader  # Import your class from the script
from rich.console import Console

console = Console()

app = FastAPI(
    title="Video Downloader API",
    description="Download videos from supported platforms like YouTube, Instagram, Twitter.",
    version="1.0.0",
)

# 🧾 Input Schema
class DownloadRequest(BaseModel):
    urls: List[HttpUrl]


@app.post("/download", summary="Download video(s) from given URL(s)")
async def download_videos(request: DownloadRequest):
    downloaded_files = []
    for url in request.urls:
        try:
            downloader = VideoDownloader(str(url))
            file_path = downloader.download()
            downloaded_files.append(file_path)
        except ValueError as ve:
            console.print(f"[red]Invalid URL: {ve}[/red]")
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")
            raise HTTPException(status_code=500, detail=f"Failed to download from: {url}")

    return {
        "message": "Download completed successfully.",
        "files": downloaded_files
    }


@app.get("/health", summary="Health check endpoint")
def health_check():
    return {"status": "ok"}
