from django.urls import include, path
from followers.views import UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('', include('accounts.urls')),  # Include the accounts app URLs as the default
    path('api/user-profiles/', UserProfileListCreateView.as_view(), name='user-profiles-list'),
    path('api/user-profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='user-profiles-detail'),
]
