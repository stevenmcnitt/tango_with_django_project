from django.http      import HttpResponse
from django.shortcuts import render
# Import the Category model.
from rango.models     import Category

# Create your views here.
def index(request):
	# Query the db for a list of all categories stored.
	# Order the categories by number of likes in descending order.
	# Retrieve the top 5 only - or all if less than 5.
    category_list = Category.objects.order_by('-likes')[:5]
    # Construct a dictionary with context_dict to pass to the template engine as its context.
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client(i.e. web browser).
    return render(request, 'rango/index.html', context_dict)