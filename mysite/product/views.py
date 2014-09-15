from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from product.models import Product
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def home(request):
	products = Product.objects.order_by('-price')
	return render(request, 'home.html', {'products': products})

def index(request):
	products = Product.objects.order_by('-price')
	return render(request, 'index.html', {'products': products})

def detail(request, id):
    product = get_object_or_404(Product, pk= id)
    return render(request, 'detail.html', {'product': product})

def search(request, search):
    match_products = Product.objects.filter(alcohol_tags=search)
    match_products = match_products.extra(order_by = ['-price'])
    return render(request, 'product/search.html', {'search' : search, 'match_products': match_products})

def login(request, search):
    match_products = Product.objects.filter(alcohol_tags=search)
    match_products = match_products.extra(order_by = ['-price'])
    return render(request, 'search.html', {'search' : search, 'match_products': match_products})

@login_required
def profile(request):
	profile = request.user.profile
	return render(request, 'profile.html', {'favorites' : profile.favorites})

@login_required
def sort_products_profile(request,sort):
	profile = request.user.profile
	favorites = profile.favorites.extra(order_by =[sort])
	return render(request, 'product/profile.html', {'sort' : sort, 'favorites' : favorites })

def sort_products(request,sort):
	if not request.POST:
		products = Product.objects.order_by(sort)
		return render(request, 'index.html', {'sort' : sort, 'products' : products })


	sortcontent = request.POST.get("sortit",None)
	if(sortcontent is None):
		return HttpResponse(status=200)


	products = Product.objects.order_by(sortcontent)
	arr = [];
	for val in products:
		dick = {};
		dick['description'] = val.description;
		dick['name'] = val.name;
		dick['price'] = val.price;
		#dick['image'] = val.image.url;
		dick['stock'] = val.stock;
		dick['id']    = val.id;
		arr.append(dick)

	print arr;
	responsedata = {}
	responsedata['description'] = sortcontent
	return render(request, 'rebuild_index.html', {'sort' : sort, 'products' : products })

	#return HttpResponse(json.dumps(arr), content_type= "application/json")
	#return render(request, 'index.html', {'sort' : sort, 'products' : products })


#def results(request, id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % id)

#def vote(request, id):
#    return HttpResponse("You're voting on product %s." % id)