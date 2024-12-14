from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header="Devloper Sania"
admin.site.site_title="Welcome to Sania's dashboard"
admin.site.index_title="Welcome to this portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact_view, name='contact')  # Corrected from contact_veiw to contact_view
]
