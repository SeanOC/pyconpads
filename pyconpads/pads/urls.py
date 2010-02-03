from django.conf.urls.defaults import *

urlpatterns = patterns('pads.views',
    (r'^$', 'pad_list'),
    url(r'^update-name/$', 'save_pad_description', name="update-description"),
    url(r'^update-date/$', 'save_pad_date', name="update-date"),
)