from django.shortcuts import render
from models import Category, Page
from forms import CategoryForm, PageForm

def index(request):
    # Showing a list of categories ordered by there likes.
    # Only showing the top 5.
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'category_list': category_list}
    return render(request, "rango/index.html", context_dict)


def about(request1):
    print 'ABOUT'
    context_dict = {'boldmessage': "I am bold font from the About page"}
    return render(request1, "rango/about.html", context_dict);

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print(form.errors)

    else:
        form = CategoryForm

    return render(request, 'rango/add_category.html', {'form':form})