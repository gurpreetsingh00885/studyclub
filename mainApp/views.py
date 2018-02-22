from django.shortcuts import render
from django import views
# Create your views here.


class HomePageView(views.View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html' , {})

home_page = HomePageView.as_view()