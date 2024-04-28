from django.shortcuts import redirect, render
from pytube import YouTube
from django.http import HttpResponse
from django.conf import settings
from yt_dlp import YoutubeDL
import os

def download_video(url):
    """
    Download a video using yt-dlp and return its title.

    Parameters:
    - url (str): The URL of the video to download.

    Returns:
    - str: The path of the downloaded video.

    """
    # Configuration for yt-dlp
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',  # Download the best quality
        'outtmpl': ('%(title)s.%(ext)s'),  # Set the output path
        # Other options can be added here
    }

    # Create a YoutubeDL instance with the specified options
    with YoutubeDL(ydl_opts) as ydl:
        # Extract information from the URL, but don't download the video
        info_dict = ydl.extract_info(url, download=False)
        ydl.download([url])

    return ydl.prepare_filename(info_dict)

def main(request):
    video_id = request.GET.get('v', None)
    return render(request,'main.html',{'video_id':video_id})

def download(request):
    try:
        # Get the video ID from the 'v' query parameter
        video_id = request.GET.get('v', None)
        if not video_id:
            return HttpResponse("Video ID not provided.")

        name=download_video(f'https://www.youtube.com/watch?v={video_id}')
        print(name)
        # Provide the file for download
        with open(f'{name}', 'rb') as video_file:
            response = HttpResponse(video_file.read(), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename={name}.mp4'
            return response
        
    except Exception as e:
        # Download the video
        return HttpResponse(str(e))
        
import os
import shutil
from django.http import JsonResponse

def delete(request):
    try:
        shutil.rmtree('downloads')
        os.mkdir('downloads')
        message = 'Deleted contents of "downloads" directory. We will never save history of your downloads.'
    except Exception as e:
        print(e)
        message = ':)'

    return JsonResponse({'message': message})


def video_details(request):
    try:
        video_id = request.GET.get('v', None)
        if not video_id:
            return JsonResponse({'error': 'Video ID not provided.'}, status=400)

        youtube = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        title = youtube.title
        thumbnail_url = youtube.thumbnail_url

        return JsonResponse({'title': title, 'thumbnail': thumbnail_url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



    # Your code here
    
    