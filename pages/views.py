from django.shortcuts import render

import operator
from pages.models import DemoQuestion

# Create your views here.
def home_en(request):
	return render(request, 'pages/home_en.html')

def home_ch(request):
	return render(request, 'pages/home_ch.html')

def demo_list(request):
	star3_demo_list = DemoQuestion.objects.filter(q_star=1)
	star4_demo_list_temp = DemoQuestion.objects.filter(q_star=2) | star3_demo_list
	star4_demo_list = sorted(star4_demo_list_temp, key=operator.attrgetter('q_id'))

	star5_demo_list_temp = DemoQuestion.objects.filter(q_star=3) | star4_demo_list_temp | star3_demo_list
	star5_demo_list = sorted(star5_demo_list_temp, key=operator.attrgetter('q_id'))

	return render(request, 'pages/demo_list.html', locals())
