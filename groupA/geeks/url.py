from django.conf.urls import url
import views
urlpatterns = [
url(r'^contact/$', views.contact),
]