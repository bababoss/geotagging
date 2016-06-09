from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from mapapp import views

urlpatterns = [
    #These are url query parameter for Analysis_tableList and Analysis_tablelDetail class
    
    url(r'^mapapp/(?P<user_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.GeoData_tableList.as_view()),
    url(r'^mapapp/detail/(?P<user_id>[0-9]+)/$',views.GeoData_tableDetail.as_view()),
    
    #These are url query parameter for Attendance_tableList and Attendance_tableDetail class
    
    #url(r'^attendance_input/$',views.Attendance_tableList.as_view()),
    #url(r'^attendance_input/(?P<pk>[0-9]+)/$',views.Attendance_tableDetail.as_view()),
    
     #this is url query parameter for index function
    
    #url(r'^index/$',views.index, name = 'index'),
    
     #this is url query parameter for home fuction 
    
    url(r'^$',views.home, name = 'home'),
    
    #this is url query parameter for Attendance_tableQuery class view
    
    #url(r'^user_state/(?P<user_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',views.Attendance_tableQuery.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)