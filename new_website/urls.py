from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('professor/',include('prof.urls')),
    path('course/',include('course.urls')),
    path('User/',include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',views.profile_page,name='profile')
]
