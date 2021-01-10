from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, "trello_app/index.html")

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