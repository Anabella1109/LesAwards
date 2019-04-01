from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
   
    url('^$',views.home,name='home'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^project/(\d+)',views.project,name ='project') ,
    # url(r'^like_home/(\d+)',views.like_home,name ='like1') ,
    # url(r'^like_post/(\d+)',views.like_post,name ='like2') ,
    # url(r'^new_comment/(\d+)',views.add_comment,name ='comment') ,
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^edit_profile/(\d+)',views.edit_profile,name ='edit_profile') ,
    url(r'^profile/(\d+)',views.profile,name ='profile') ,
    url(r'^grade/(\d+)',views.grade_project,name ='grade') ,
     url(r'^api/profiles/$', views.ProfileList.as_view()),
     url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view())
    # url(r'^unfollow/(\d+)',views.unfollow_profile,name ='follow') ,
    # url(r'^followers/(\d+)',views.who_followers,name ='followers') ,   
    # url(r'^following/(\d+)',views.who_following,name ='following') , 

   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)