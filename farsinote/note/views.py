from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import Note


def index(request):
    note_list = Note.objects.all()
    context = {'note_list': note_list}
    return render(request, 'note/index.html', context)


def create(request):
    return HttpResponse('this is the create note form')


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/detail.html', {'note': note})


def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        date = datetime.datetime.now()
        n = Note(title=title, created_date=date, body=body)
        n.save()



        return render(request, 'note/new.html')

    return render(request, 'note/new.html')


    return rend

