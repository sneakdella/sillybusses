from django.shortcuts import render

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

	return render (
		request,
		'sb/upload.html',
		{
			'test': test,
		}
	)
