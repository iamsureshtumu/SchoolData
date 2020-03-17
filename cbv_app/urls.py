from django.urls import path,re_path
from cbv_app import views

app_name="cbv_app"

urlpatterns = [
    path('school',views.SchoolListView.as_view(),name="list"),
    re_path(r'^(?P<pk>\d+)/',views.SchoolDetailView.as_view(),name='detail_view'),
    path('create/',views.SchoolCreateView.as_view(),name="create"),
    re_path(r'^update/(?P<pk>\d+)/',views.SchoolUpdateView.as_view(),name='update_view'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
##########################################################################################
    path('student/',views.StudentListView.as_view(),name="studentlist"),
    re_path(r'^(?P<pk>\d+)/',views.StudentDetailView.as_view(),name='studentdetail_view'),
    path('studentcreate/',views.StudentCreateView.as_view(),name="studentcreate"),
    re_path(r'^update/(?P<pk>\d+)/',views.StudentUpdateView.as_view(),name='studentupdate_view'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='studentdelete'),

]
