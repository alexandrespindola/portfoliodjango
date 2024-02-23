from django.contrib import admin
from django.urls import include, path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('thank-you-contact/', views.thank_you_contact, name='thank-you-contact'),

]