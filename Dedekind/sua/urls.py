from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'sua'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sua/admin$', views.adminIndex, name='admin-index'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^apply_sua$', views.apply_sua, name='apply_sua'),
    url(r'^appeal_for$', views.appeal_for, name='appeal_for'),
    url(
        r'^application/(?P<pk>[0-9]+)/$',
        login_required(views.ApplicationDetailView.as_view()),
        name='application_detail',
    ),
    url(
        r'^data/StudentList',
        login_required(views.JSONStudentListView.as_view()),
        name='data_StudentList',
    ),
    url(
        r'^data/StudentSuaList/([0-9]+)/$',
        login_required(views.JSONStudentSuaListView.as_view()),
        name='data_StudentSuaList',
    ),
    url(
        r'^Student/(?P<pk>[0-9]+)/$',
        login_required(views.StudentDetailView.as_view()),
        name='Student-Detail',
    ),
    url(
        r'^Student/add/$',
        login_required(views.StudentCreate.as_view()),
        name='student-add',
    ),
    url(
        r'^Student/(?P<pk>[0-9]+)/update/$',
        login_required(views.StudentUpdate.as_view()),
        name='student-update',
    ),
    url(
        r'^Student/(?P<pk>[0-9]+)/delete/$',
        login_required(views.StudentDelete.as_view()),
        name='student-delete',
    ),
]
