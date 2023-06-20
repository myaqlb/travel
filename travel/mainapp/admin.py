from django.contrib import admin

# Register your models here.
from mainapp.models import News, Tour, Hotels, FeedBack

admin.site.register(News)
admin.site.register(Hotels)
admin.site.register(Tour)
admin.site.register(FeedBack)