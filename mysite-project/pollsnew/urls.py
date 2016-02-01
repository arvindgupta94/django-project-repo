from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.index,name='index'),
url(r'^arvind/$',views.arvind),
url(r'^category/(?P<category_id>[0-9]+)/$',views.categoryDetail,name='categoryDetail'),
url(r'^question/(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
url(r'^category/all/$',views.categoryAll,name='categoryAll'),
url(r'^category/add/$',views.categoryAdd,name='categoryAdd'),
url(r'^question/(?P<question_id>[0-9]+)/choice/add/$',views.choiceAdd,name='choiceAdd'),\
url(r'^category/(?P<category_id>[0-9]+)/question/add/$',views.questionAdd,name='questionAdd'),
url(r'^question/(?P<question_id>[0-9]+)/$',views.questionDetail,name='questionDetail'),
url(r'^register/$', views.register, name='register'),
url(r'^profile/[a-z]+/$',views.profile,name='profile'),
]