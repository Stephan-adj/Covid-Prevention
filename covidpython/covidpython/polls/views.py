from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Poll


def home(request):
    context = {
        'Polls': Poll.objects.all()
    }
    return render(request, 'polls/home.html', context)


class PollListView(ListView):
    model = Poll
    template_name = 'polls/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PollDetailView(DetailView):
    model = Poll


class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.email = self.request.user
        return super().form_valid(form)


class PollUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Poll
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.email = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Poll = self.get_object()
        if self.request.user == Poll.email:
            return True
        return False


class PollDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Poll
    success_url = '/'

    def test_func(self):
        Poll = self.get_object()
        if self.request.user == Poll.email:
            return True
        return False


def about(request):
    return render(request, 'polls/about.html', {'title': 'About'})
	
class AboutView(ListView):
    model = Poll
    template_name = 'polls/about.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']