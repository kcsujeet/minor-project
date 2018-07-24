from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Item,Detail
from django.db.models import Q

class IndexView(generic.ListView):
    template_name ='category/index1.html'

    def get_queryset(self):
        return Item.objects.all()


def ItemView(request):
    page = request.GET.get('page', 1)

    if "search" in request.GET:

        itemlist = Item.objects.filter(
            Q(itemname__icontains=request.GET["search"]) | Q(item_status__icontains=request.GET["search"]))
        paginator = Paginator(itemlist, 8)
        try:
            item_list = paginator.page(page)
        except PageNotAnInteger:
            item_list = paginator.page(1)
        except EmptyPage:
            item_list = paginator.page(paginator.num_pages)
        return render(request, 'category/index1.html',
                          {'item_list': item_list, 'searchvalue': request.GET["search"]})

    else:

        itemlist = Item.objects.all()
        paginator = Paginator(itemlist, 8)


        try:
            item_list = paginator.page(page)
        except PageNotAnInteger:
            item_list = paginator.page(1)
        except EmptyPage:
            item_list = paginator.page(paginator.num_pages)
        return render(request, 'category/index1.html', {'item_list': item_list})

def ItemsearchView(request):

    page = request.GET.get('page', 1),
    search = request.GET.get("search",)
    print (search)

    itemlist = Item.objects.filter(Q(item_name__icontains=request.GET["search"]) | Q(item_status__item_name__icontains=request.GET["search"]))
    paginator = Paginator(itemlist, 8)
    item_list = paginator.page(page)
    return render(request, 'tac/index1.html',
                      {'item_list': item_list, 'searchvalue': request.GET["search"]})


class DetailView(generic.DetailView):
    model=Item
    template_name='category/detail.html'


class ItemCreate(CreateView):
    model =Item
    fields = ['item_logo','item_name','item_status','item_price']

