from django.contrib import admin
from django.urls import path
from . import views
app_name='prof'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:professor_id>/',views.detail,name='detail'),
    path('<int:professor_id>/add_review/',views.ReviewFormView.as_view(),name='add_review'),
    path('search',views.SearchView.as_view(),name='search'),
    path('<int:professor_id>/edit_review/<int:review_id>/', views.ReviewFormUpdate.as_view(), name='edit_review'),
    path('<int:professor_id>/delete_review/<int:review_id>/', views.ReviewFormDelete.as_view(), name='delete_review')
]
#path('<int:professor_id>/add_review/',views.review,name='add_review')