#urls posts

from django.conf.urls import url
from django.contrib  import admin

from .views import (
	index_call,
	reel_call,
	)

urlpatterns = [

	url(r'^$', index_call, name = 'indexCall'),
	url(r'^reel/$', reel_call, name = 'reelCall'),

]