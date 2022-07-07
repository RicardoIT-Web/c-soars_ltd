from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File


def upload(request):
    """ A view for file and media uploads """
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        filestorage = FileSystemStorage()
        name = filestorage.save(uploaded_file.name, uploaded_file)
        context['url'] = filestorage.url(name)
    return render(request, 'administration/upload.html', context)


def files_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_list')
    else:
        form = FileForm()
    return render(request, 'administration/files_upload.html', {
        'form': form
    })


def files_list(request):
    files = File.objects.all()
    return render(request, 'administration/files_list.html', {
        'files': files
    })
