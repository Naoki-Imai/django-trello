from django.shortcuts import render,redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, ListForm
from .models import List
from .mixins import OnlyYouMixin


# Create your views here.
def index(request):
  return render(request, "trello_app/index.html")

#ログインしたらhomeへリダイレクトする
@login_required
def home(request):
  return render(request, "trello_app/home.html")

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user_instance = form.save()
      login(request, user_instance)
      return redirect('trello_app:home')
  else:
    form = UserCreationForm()

  context = {
    "form":form
  }
  return render(request, 'trello_app/signup.html', context)

class UserDetailView(LoginRequiredMixin, DetailView):
  model = User
  template_name = "trello_app/users/detail.html"

class UserUpdateView(OnlyYouMixin,UpdateView):
  model = User
  template_name = "trello_app/users/update.html"
  form_class = UserForm
# resolve_url 正常ならusers_detaiに接続する.pkはDBのpk
  def get_success_url(self):
    return resolve_url('trello_app:users_detail', pk=self.kwargs['pk'])

class ListCreateView(LoginRequiredMixin, CreateView):
  model = List
  template_name = 'trello_app/lists/create.html'
  form_class = ListForm
  success_url = reverse_lazy('trello_app:lists_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ListListView(LoginRequiredMixin, ListView):
  model = List
  template_name = 'trello_app/lists/list.html'

class ListDetailsView(LoginRequiredMixin, DetailView):
  model = List
  template_name = 'trello_app/lists/detail.html'

class ListUpdateView(LoginRequiredMixin,UpdateView):
  model = List
  template_name = "trello_app/lists/update.html"
  form_class = ListForm
# resolve_url 正常ならusers_detaiに接続する.pkはDBのpk
  def get_success_url(self):
    return resolve_url('trello_app:lists_detail', pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
  model = List
  template_name = 'trello_app/lists/delete.html'
  form_class = ListForm
  success_url = reverse_lazy('trello_app:lists_list')