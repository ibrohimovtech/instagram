from django.urls import path
from .views import UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),  # Change the URL pattern to empty for the login view
]
