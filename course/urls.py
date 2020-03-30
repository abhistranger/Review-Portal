from django.contrib import admin
from django.urls import path
from . import views
from .models import reviews

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/',views.detail,name='detail'),
    path('<int:course_id>/add_review/',views.ReviewFormView.as_view(),name='add_review'),
    path('search',views.SearchView.as_view(),name='search'),
    path('<int:course_id>/edit_review/<int:review_id>/', views.ReviewFormUpdate.as_view(), name='edit_review'),
    path('<int:course_id>/delete_review/<int:review_id>/', views.ReviewFormDelete.as_view(), name='delete_review')
]
