from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterUserForm, LoginUserForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Profile
from news.models import Categories



class register_home(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register_home.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('register_page_2')

    def get_context_data(self, **kwargs):
        categories = Categories.objects.all()
        context = super(CreateView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context


def register_page2(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = request.user
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    date = {
        'form': form,
        'error': 'Форма была неверной',
    }
    categories = Categories.objects.all()
    return render(request, 'register/register_page_2.html', {'date': date, 'categories': categories})


def redact(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.filter(profile_id=request.user.id).update(profile_img=f"images/profile_img/{request.FILES.get('profile_img')}", bio=request.POST['bio'])
            return redirect('profile')

    else:
        form = ProfileForm()
    categories = Categories.objects.all()
    date = {
        'form': form,
        'error': 'Форма была неверной',
        'categories': categories,
    }

    return render(request, 'register/redact_profile.html', date)


class LogInUser(LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        categories = Categories.objects.all()
        context = super(LogInUser, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context


def logOutUser(request):
    logout(request)
    return redirect('login')

