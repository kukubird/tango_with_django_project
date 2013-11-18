from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'), #for Category
        url(r'^add_category/$', views.add_category, name='add_category'), #for add_category form
		#url(r'^add_page/', views.add_page, name='add_page'), #url for add_Page form
		url(r'^category/(?P<category_name_url>[a-z A-Z _ 0-9]+)/add_page/$', views.add_page, name='add_page'), # for add_page agin becausethe previous function was asinged two aguments so this was to all us to access the page withou adding arguments.
		url(r'^register/$', views.register, name='register'), #url for register form
		url(r'^login/$', views.user_login, name='login'),#url for the login page
		url(r'^restricted/', views.restricted, name='restricted'),#url for restricting acess
		url(r'^logout/$', views.user_logout, name='logout'), #url for logout
		url(r'^profile/$', views.profile, name='profile'), #url for profile
		url(r'^goto/$', views.track_url, name='track_url'), #url for track_url so it updates the views
		url(r'^like_category/$', views.like_category, name='like_category'), #url for like_category
		url(r'^suggest_category/$', views.suggest_category, name='suggest_category'), #url for suggest_category
)


