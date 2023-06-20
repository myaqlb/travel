from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.forms import MailForm
from mainapp.models import News, Tour
from travel import settings


def index(request):
    news = News.objects.all()[:6]
    tour_max = Tour.objects.all()[:2]
    tour_min = Tour.objects.all()[2:6]

    context = {
        'title': 'Новости',
        'news': news,
        'tour_max': tour_max,
        'tour_min': tour_min,
    }
    return render(request, 'mainapp/index.html', context)

def feedback(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            messages = f'От: {form.last_name} ({form.email})\nИмя: {form.first_name}\nВыбор: {form.select}'
            res = send_mail(settings.EMAIL_TITLE, messages, settings.EMAIL_HOST_USER, ['ustyugov04@inbox.ru'])
            if res:
                form.save()
                return HttpResponseRedirect(reverse('mainapp:feedback'))
    else:
        form = MailForm()
    context = {
        'form': form
    }
    return render(request, 'mainapp/feedback.html', context)

def select_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    context = {
        'title': tour.name,
        'tour': tour,
    }
    return render(request, 'mainapp/select_tour.html', context)


def select_news(request, id):
    news = get_object_or_404(News, id=id)
    context = {
        'title': news.name,
        'news': news
    }
    return render(request, 'mainapp/select_news.html', context)
