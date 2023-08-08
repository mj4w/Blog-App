from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<str:pk>/',views.postdetails ,name='post-details'),
    path('category/',views.category, name='category'),
    path('users/',views.users, name='users'),
    path('user-reg/',views.user_registration,name='user-register'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)