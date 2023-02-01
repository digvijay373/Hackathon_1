from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from index.forms import UploadForm

from django.core.cache import caches

# cache = caches['redis']


def home(request):
    return HttpResponse("This is home")

def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse("form submitted succesfully")
    return render(request, 'Form/upload.html', {'form' : UploadForm})