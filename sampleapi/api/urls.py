from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import HelloView

urlpatterns = [
    path('hello/', HelloView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
