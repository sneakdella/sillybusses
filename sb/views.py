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