from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
from .forms import *
from blog.decorators import *


@user_is_superuser
def home(request):
    return render(request, 'media_dashboard.html')


@user_is_superuser
def Sahih_Muslim_Upload(request):
    form = AudioUpload()
    if request.method == 'POST':
        title = request.POST.get('title')
        form = AudioUpload(request.POST, request.FILES or None)
        if form.is_valid:
            if SahihMuslim.objects.filter(title=title).exists():
                messages.warning(
                    request, f'Audio with {title} title already Exist!')
                return render(request, 'sahih_muslim.html', {'form': form})
            form.save()
            messages.success(
                request, f'Audio File {title} Was Successfully Uploaded!')
            return redirect('Sahih_Muslim_View')

    return render(request, 'sahih_muslim_upload.html', {'form': form})


def Sahih_Muslim_View(request):
    sahih_muslim = SahihMuslim.objects.all().order_by('-title')

    context = {'sahih_muslim': sahih_muslim}
    return render(request, 'sahih_muslim_view.html', context)
