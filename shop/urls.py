from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>', views.single_course, name='single_course'),
]
