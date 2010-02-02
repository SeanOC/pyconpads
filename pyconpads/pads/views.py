from annoying.decorators import render_to, ajax_request

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
def save_pad_name(request):
    id = request.POST.get('id', None)
    name = request.POST.get('value', None)
    pad = get_object_or_404(Pad, id=id)
    if not name:
        raise Http404
        
    meta, created = PadMeta.objects.get_or_create(pad=pad, defaults={'name': name})
    if not created:
        meta.name = name
        meta.save()
        
    return {'name': meta.name}