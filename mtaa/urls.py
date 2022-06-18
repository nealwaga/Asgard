from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Create urls here 
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^editprofile/$', views.edit_profile, name='edit_profile'),
    url(r'^new/business', views.new_business, name='add_business'),
    url(r'^join/(\d+)', views.join, name='join'),
    url(r'^myhood/$', views.hoods, name='hood'),
    url(r'^exitHood/(\d+)', views.exitHood, name='exitHood'),
    url(r'^createpost/$', views.create_post, name='create_post'),
    url(r'^createhood/$', views.create_hood, name='create_hood'),
    url(r'^deletepost/(\d+)', views.delete_post, name='delete_post'),
    url(r'^search/$', views.search, name='search'),
    url(r'^deletehood/(\d+)', views.delete_hood, name='delete_hood'),
    url(r'^updatehood/(\d+)', views.update_hood, name='update_hood'),
    url(r'^occupants/(?P<hood_id>\d+)', views.occupants, name='occupants'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)