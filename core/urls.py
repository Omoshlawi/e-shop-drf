from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.ApiRootView.as_view(), name='root'),
]