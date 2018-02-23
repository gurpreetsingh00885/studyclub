from django.shortcuts import render
from django import views
from mainApp.forms import VidOpenForm
from embed_video.backends import detect_backend
# Create your views here.


class HomePageView(views.View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html' , {})

home_page = HomePageView.as_view()

class VideoSearchView(views.View):
	def get(self, request, *args, **kwargs):
		form = VidOpenForm()
		return render(request, 'vidsearch/index.html' , {"form": form})

	def post(self, request, *args, **kwargs):
		print(request.POST)
		video = detect_backend(request.POST['url'])
		cc_url = "https://www.youtube.com/api/timedtext?lang=en&v=%s" %(video.get_code())
		vid_url = video.get_code()
		return render(request, 'vidsearch/view.html', {"my_video": video, "cc_url": cc_url, 'vid_url': vid_url})

vid_search_page = VideoSearchView.as_view()