from django.shortcuts import render, render_to_response
from .models import Project, Category, Method, Status, StarLevel, Question, Result
from django.http import HttpResponse
from django.template import loader, Context
from django.template.loader import get_template

# Create your views here.
def count_function(input_query):
	pass_count = 0.0
	fail_count = 0.0
	pending_count = 0.0
	total_count = len(input_query)

	for item in input_query:
		if item.status.status_name == 'pass':
			pass_count+=1
		elif item.status.status_name == 'fail':
			fail_count+=1
		else:
			pending_count+=1

	pass_percent = round((pass_count/total_count)*100, 1)
	fail_percent = round((fail_count/total_count)*100, 1)
	pending_percent = round((pending_count/total_count)*100, 1)

	return pass_percent, fail_percent, pending_percent


# def result(request):
# 	return render(request, 'tform/result.html')

def quzpage(request):

	result_list = Result.objects.filter(result_id=1)
	pass_percent, fail_percent, pending_percent = count_function(result_list)

	return render(request, 'tform/result_body.html', locals())
	# return render_to_response('tform/result.html', {'result_list':result_list}, Context)
	# context = {}
	# results = Result.objects.all()
	# context['result'] = results
	# t = get_template('tform/detail.html')
	# html = t.render(Context(context))

	# return HttpResponse(html)
	# results = Result.objects.all()
	# return render(request, 'tform/detail.html',locals())


# def detail(request, pk):
# 	result_list = Result.objects.filter(result_id=1).filter(question__q_category__pk=pk)
# 	pass_percent, fail_percent, pending_percent = count_function(result_list)
# 	category_name = Category.objects.filter(pk=pk)[0].category_name

# 	return render(request, 'tform/detail.html', locals())