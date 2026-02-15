from django.shortcuts import render
from rango.models import Category

def index(request):
    # Query the database for a list of all categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if at least 5 don't exist.
    category_list = Category.objects.order_by('-likes')[:5]
    
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    
    # Return a rendered response to send to the client.
    return render(request, 'rango/index.html', context=context_dict)