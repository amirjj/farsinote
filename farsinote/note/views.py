from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
import datetime
from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note/index.html'
    context_object_name = 'note_list'
    ordering = ['-created_date']
    paginate_by = 4


def create(request):
    return HttpResponse('this is the create note form')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note

    success_url = "/note/"
    # template_name = 'note/detail.html'
    # context_object_name = 'note'



class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']


# class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'body']

    # def test_func(self):
    #     note = self.get_object()
    #     if note.author == self.request.user:
    #         return True
    #     return False


# def new(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         body = request.POST['body']
#         date = datetime.datetime.now()
#         n = Note(title=title, created_date=date, body=body)
#         n.save()
#
#     return render(request, 'note/new.html')

