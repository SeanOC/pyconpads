from annoying.decorators import render_to, ajax_request
from dateutil.parser import parse as parse_date

from django.http import Http404
from django.shortcuts import get_object_or_404

from pads.models import Pad, PadMeta

@render_to('list.html')
def pad_list(request):
    pads = Pad.objects.all().order_by('id').select_related('padmeta')
    
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
        
    return {'date': date.strftime('%m/%d %H:%M')}