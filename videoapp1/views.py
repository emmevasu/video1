from django.shortcuts import render,redirect
from .models import Video
from .forms import VideoForm
from django.http import HttpResponse
from filetransfers.api import serve_file
from django.shortcuts import get_object_or_404


def showvideo(request):
    lastvideo = Video.objects.last()

    videofile = lastvideo

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'Blog/videos.html', context)


def download_handler(request, pk):
    upload = get_object_or_404(Video, pk=pk)
    return serve_file(request, 'Video1.file',{'upload':upload})
# def getvideo(request):
#     lst=Video.objects.last()
#     form=VideoForm(request.POST)
#     return render(request,'Blog/Video1.html',{'lst':lst,'form':form})
#


# Create your views here.
class Download_handler(object):
    pass