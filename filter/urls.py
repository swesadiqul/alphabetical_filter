from django.urls import path
from filter import views


urlpatterns = [
    path('', views.index, name='home'),
    path('filter_data', views.filter_data, name='filter_data'),
]
