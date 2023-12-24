from django.urls import path

from .views import SignUpView
from .views import HomePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', HomePageView.as_view(), name='home'),]