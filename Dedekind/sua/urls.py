from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'sua'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^playMFS$', views.playMFS, name='playMFS'),
    url(r'^admin/$', views.adminIndex, name='admin-index'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^apply_sua$', views.apply_sua, name='apply_sua'),
    url(r'^appeal_for$', views.appeal_for, name='appeal_for'),
    url(
        r'^student/list$',
        login_required(views.JSONStudentListView.as_view()),
        name='student-list-json',
    ),
    url(
        r'^student/([0-9]+)/sualist$',
        login_required(views.JSONStudentSuaListView.as_view()),
        name='student-sualist-json',
    ),
    url(
        r'^sua/([0-9]+)/application$',
        login_required(views.JSONSuaApplicationView.as_view()),
        name='sua-application-json',
    ),
    url(
        r'^sua/([0-9]+)/gsua$',
        login_required(views.JSONSuaGSuaListView.as_view()),
        name='sua-gsua-json',
    ),
    url(
        r'^application/checklist$',
        login_required(views.JSONApplicationCheckListView.as_view()),
        name='application-checklist-json',
    ),
    url(
        r'^gsuap/list$',
        login_required(views.JSONGSuaPublicityListView.as_view()),
        name='gsuap-list-json',
    ),
    url(
        r'^gsua/([0-9]+)/sualist$',
        login_required(views.JSONGSuaSuaListView.as_view()),
        name='gsua-sualist-json',
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
    url(
        r'^application/(?P<pk>[0-9]+)/$',
        login_required(views.Sua_ApplicationDetailView.as_view()),
        name='application-detail',
    ),
    url(
        r'^application/student/([0-9]+)/add$',
        login_required(views.Sua_ApplicationCreate.as_view()),
        name='application-add',
    ),
    url(
        r'^application/(?P<pk>[0-9]+)/update$',
        login_required(views.Sua_ApplicationUpdate.as_view()),
        name='application-update',
    ),
    url(
        r'^application/(?P<pk>[0-9]+)/delete/$',
        login_required(views.Sua_ApplicationDelete.as_view()),
        name='application-delete',
    ),
    url(
        r'^application/(?P<pk>[0-9]+)/check/$',
        login_required(views.Sua_ApplicationCheck.as_view()),
        name='application-check',
    ),
    url(
        r'^gsuap/(?P<pk>[0-9]+)/$',
        login_required(views.GSuaPublicityDetailView.as_view()),
        name='gsuap-detail',
    ),
    url(
        r'^gsuap/add$',
        login_required(views.GSuaPublicityCreate.as_view()),
        name='gsuap-add',
    ),
]
