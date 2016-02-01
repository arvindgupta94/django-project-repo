from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.index,name='home_page'),
url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='result'),
url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
url(r'^contact/$',views.ContactView,name='contact'),
]