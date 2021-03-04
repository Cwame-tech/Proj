from django.urls import path
from .views import (
    PostListView,
)
from .import views
urlpatterns = [
    
    path('',views.index, name = 'indeex'),
    path('speech/', PostListView.as_view(), name = 'speech'),
    path('about/', views.about, name = 'EndOf-about'),
    path('about/', views.about, name = 'EndOf-about'),
    path('speaker/',views.Speakview, name = 'speaker_detail'),
]