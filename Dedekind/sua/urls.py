from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'sua'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.adminIndex, name='admin-index'),
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
        r'^json/student/list',
        login_required(views.JSONStudentListView.as_view()),
        name='student-list-json',
    ),
    url(
        r'^json/student/([0-9]+)/sualist$',
        login_required(views.JSONStudentSuaListView.as_view()),
        name='student-sualist-json',
    ),
    url(
        r'^student/(?P<pk>[0-9]+)/$',
        login_required(views.StudentDetailView.as_view()),
        name='student-detail',
    ),
    url(
        r'^student/add/$',
        login_required(views.StudentCreate.as_view()),
        name='student-add',
    ),
    url(
        r'^student/(?P<pk>[0-9]+)/update/$',
        login_required(views.StudentUpdate.as_view()),
        name='student-update',
    ),
    url(
        r'^student/(?P<pk>[0-9]+)/delete/$',
        login_required(views.StudentDelete.as_view()),
        name='student-delete',
    ),
]
