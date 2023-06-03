from django.urls import path
from app.views import TranslateAPIView

urlpatterns = [
    path('translate', TranslateAPIView.as_view(), name='translate'),
]
