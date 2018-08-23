from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),

    path('post/create', views.CreateView.as_view(), name='create'),

    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('post/<int:pk>/update', views.UpdateView.as_view(), name='update'),

    path('post/<int:pk>/delete', views.DeleteVew.as_view(), name='delete')

]