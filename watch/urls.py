from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#Create urls here
urlpatterns = [
    path('',views.index, name='index'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('update-profile',views.update_profile, name='update_profile'), 
    path('profile/<pk>',views.profile, name = 'profile'),
    path('create-hood',views.createhood, name='createhood'), 
    path('neighbourhood/<id>',views.neighbourhood, name = 'neighbourhood'),
    path('post/<hood_id>',views.post, name = 'post'), 
    path('business/<id>',views.createbusiness, name = 'createbusiness'),
    path('search/',views.search_results, name='search_results'),
    path('join_neighbourhood/<id>', views.join_neighbourhood, name='join-neighbourhood'),
    path('move_neighbourhood/<id>', views.move_neighbourhood, name='move-neighbourhood'),
]

