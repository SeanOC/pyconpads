from annoying.decorators import render_to, ajax_request
from dateutil.parser import parse as parse_date

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
from django.core.urlresolvers import reverse

from pads.models import Pad, PadMeta

def expire_page(path, key_prefix=None):
    '''
    Delete page from cache based on it's url
    '''
    request = HttpRequest()
    request.path = path    
    key = get_cache_key(request, key_prefix)
    if cache.has_key(key):
        cache.delete(key)

@cache_page(300)
@render_to('list.html')
def pad_list(request):
    pads = Pad.objects.all().select_related('meta').order_by('id')
    
    return {
        'pads': pads,
    }

@ajax_request
def save_pad_description(request):
    id = request.POST.get('id', None)
    description = request.POST.get('value', None)
    pad = get_object_or_404(Pad, id=id)
    if not description:
        raise Http404
        
    meta, created = PadMeta.objects.get_or_create(pad=pad, defaults={'description': description})
    if not created:
        meta.description = description
        meta.save()
        
    expire_page(reverse('list-pads'))
        
    return {'description': meta.description}
    
@ajax_request
def save_pad_date(request):
    id = request.POST.get('id', None)
    date = request.POST.get('value', None)
    pad = get_object_or_404(Pad, id=id)
    if not date:
        raise Http404
    
    date = parse_date(date)
    
    meta, created = PadMeta.objects.get_or_create(pad=pad, defaults={ 'talk_time': date})
    if not created:
        meta.talk_time = date
        meta.save()
    
        
    expire_page(reverse('list-pads'))
        
    return {'date': date.strftime('%m/%d %H:%M')}