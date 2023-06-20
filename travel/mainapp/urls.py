from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('select/tour/<int:id>/', mainapp.select_tour, name='select_tour'),
    path('select/news/<int:id>/', mainapp.select_news, name='select_news'),

    path('feedback/', mainapp.feedback, name='feedback'),
]