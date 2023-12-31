from django.shortcuts import redirect, render
from pytube import YouTube
from django.http import HttpResponse
from django.conf import settings
import os

def main(request):
    video_id = request.GET.get('v', None)
    return render(request,'main.html',{'video_id':video_id})

def download(request):
    try:
        # Get the video ID from the 'v' query parameter
        video_id = request.GET.get('v', None)
        if not video_id:
            return HttpResponse("Video ID not provided.")

        # Create YouTube object
        youtube = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        print(youtube)
        # Get the highest resolution stream
        video_stream = youtube.streams.get_highest_resolution()
        print(video_stream)
        # Set the file path including the video title
        
        # Download the video
        name=video_stream.download(output_path=f'downloads\\', filename=f'{youtube.title}'+'.mp4')
        print(name)
        # Provide the file for download
        with open(f'{name}', 'rb') as video_file:
            response = HttpResponse(video_file.read(), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename={youtube.title}.mp4'
            return response
        
    except Exception as e:
        # Download the video
        print(e)
        name=video_stream.download(output_path=f'downloads\\', filename=f'{video_id}'+'.mp4')
        # Provide the file for download
        with open(f'{name}', 'rb') as video_file:
            response = HttpResponse(video_file.read(), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename={video_id}.mp4'
            return response
        
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


from django.http import JsonResponse

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


