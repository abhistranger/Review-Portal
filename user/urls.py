from . import views
from django.urls import path

urlpatterns=[
    path('register/',views.UserFormView.as_view(),name='register'),
]
