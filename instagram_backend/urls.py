from django.urls import include, path

urlpatterns = [
    path('', include('accounts.urls')),  # Include the accounts app URLs as the default
    # Add other app URLs here if needed
]
