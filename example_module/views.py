from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ChosePath

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChosePath(request.POST)
        # check whether it's valid:
        if form.is_valid():
            text_input = form.cleaned_data['named_form_value']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/{}/'.format(text_input))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ChosePath()

    return render(request, 'example_templates/example.html', {'form': form})
    # values = request.GET.get('level', '0')
    # return HttpResponse("Hello, world. You're at the polls index." + values)
# Create your views here.
