from django.shortcuts import render
from django import views
from mainApp.forms import VidOpenForm
# Create your views here.


class HomePageView(views.View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html' , {})

home_page = HomePageView.as_view()

class VideoSearchView(views.View):
	def get(self, request, *args, **kwargs):
		form = VidOpenForm()

		return render(request, 'vidsearch/index.html' , {"form": form})

vid_search_page = VideoSearchView.as_view()