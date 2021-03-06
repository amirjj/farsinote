from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)
import datetime
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'note/index.html'
    context_object_name = 'note_list'
    ordering = ['-created_date']


def create(request):
    return HttpResponse('this is the create note form')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'body']



# def new(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         body = request.POST['body']
#         date = datetime.datetime.now()
#         n = Note(title=title, created_date=date, body=body)
#         n.save()
#
#     return render(request, 'note/new.html')

