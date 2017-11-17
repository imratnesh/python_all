from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),	
    url(r'^login/', views.login, name='login'),
   # url(r'^register/',TemplateView.as_view(template_name='ratneshapp/template/register.html')),
    url(r'^saved/', views.SaveLogonForm, name='saved')		
]
