from annoying.decorators import render_to

from pads.models import Pad

@render_to('list.html')
def pad_list(request):
    pads = Pad.objects.all().order_by('id')
    
    return {
        'pads': pads,
    }
