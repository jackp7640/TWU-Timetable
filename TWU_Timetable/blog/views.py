from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Jack Park',
		'title': 'Blog post 1',
		'content': 'first post content',
		'date_posted': 'March 13, 2020'
	},
	{
		'author': 'Jack Park',
		'title': 'Blog post 2',
		'content': 'second post content',
		'date_posted': 'March 14, 2020'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})


