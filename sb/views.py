from django.shortcuts import render, redirect
from .forms import SyllabusForm

# Create your views here.


def index (request):
	""" Renders Home Page """
	test = "test"

	return render (
		request,
		'sb/index.html',
		{
			'test': test,
		}
	)

def search (request):
	""" Renders Search Page """
	test = "test"

	return render (
		request,
		'sb/search.html',
		{
			'test': test,
		}
	)

def upload (request):
	""" Renders upload Page """
	test = "test"

	if request.method == 'POST':
		form = SyllabusForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = SyllabusForm()
	return render(request, 'sb/upload.html', {
		'form': form
    })