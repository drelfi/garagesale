# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from garagesale.models import Item, Screenshots, ContactRequest

def index(request, cpartner=''):
    items = Item.objects.filter(partner=cpartner)

    partners = Item.objects.all().values_list('partner', flat=True).exclude(partner='').distinct()
    
    context = { "catalog_items": items, 'partners': partners, 'partner': cpartner, } 
    return render( request, 'index.html', context )

def detail(request, item_id):
    
    ss = Screenshots.objects.filter( item_id = item_id )
    i = get_object_or_404(Item, pk=item_id)

    context = { 'screenshots': ss, 'item': i }
    return render( request, 'detail.html', context)

def contact(request, item_id):
    i = get_object_or_404(Item, pk=item_id)
    if request.method == 'GET':
        
        context = {'item': i}
        return render(request, 'contact.html', context)
    elif request.method == 'POST':
        req = ContactRequest()
        req.name = request.POST['name']
        req.email = request.POST['email']
        req.message = request.POST['question']
        req.item = i
        if (req.email is not None and len(req.email.strip()) > 0) and (req.name is not None and len(req.name.strip()) > 0):
            req.save()
        if len(i.partner) > 0:
            return HttpResponseRedirect(reverse('partner-index', args=(i.partner,)))
        else:
            return HttpResponseRedirect(reverse('index'))