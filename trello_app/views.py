from django.shortcuts import render,redirect, resolve_url
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from .forms import UserForm
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
