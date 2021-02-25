from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
import datetime
from .models import Note


class IndexView(generic.ListView):
    template_name = 'note/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        return Note.objects.all()


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

