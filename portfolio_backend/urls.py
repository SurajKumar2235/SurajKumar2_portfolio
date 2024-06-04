from django.contrib import admin
from django.urls import path
from portfolio import views
from portfolio.views import ProjectsAPIView,HomeView,ContactAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/projects/',ProjectsAPIView.as_view(),name='projects_api'),
    path('api/contact/', ContactAPIView.as_view(), name='contact-api'),

]
