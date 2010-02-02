from django.conf.urls.defaults import *

urlpatterns = patterns('pads.views',
    (r'^$', 'pad_list'),
    url(r'^update-name/$', 'save_pad_name', name="update-name"),
)