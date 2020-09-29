from django.conf.urls import url
from . import views
 
urlpatterns=[
	url(r'^home/', views.index,name='index'),
	url(r'^login/',views.login,name='login'),
	url(r'^registration/',views.registration,name='registration'),
	url(r'^data/$', views.data, name='data'),
	url(r'^get_data/$', views.get_data, name='get_data'),
	url(r'^dash/$',views.dash,name='dashboard'),
	url(r'^logout/$',views.logout,name='dashboard'),
	url(r'^edit/$',views.edit,name='profile_edit'),
	url(r'^bike/$',views.order_bike,name='order_comp'),
	url(r'^rep/$',views.order_rep,name='order_rep'),



	url(r'^yamaha/$',       views.yamaha,name='order_dell1'),
	url(r'^harleyDavidson/$',     views.harleyDavidson,name='order_dell1'),
	
	url(r'^gb/$',   views.gb,name='order_dell1'),
	url(r'^en/$',      views.en,name='order_dell1'),
	url(r'^sp/$',    views.sp,name='order_dell1'),



	url(r'^edit_data/$',views.edit_data,name='edit_data')
]
 