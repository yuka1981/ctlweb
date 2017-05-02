from django.shortcuts import render, render_to_response
from .models import Project, Category, Method, Status, StarLevel, Question, Result
from django.http import HttpResponse
from django.template import loader, Context
from django.template.loader import get_template

import operator

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
def select_category(result_id, category_pk):

	result_list = Result.objects.filter(result_id=result_id).filter(question__q_category__pk=category_pk)

	return result_list

def select_package(result_id, q_star_pk):

	result_list = Result.objects.filter(result_id=result_id).filter(question__q_star__pk=q_star_pk)

	return result_list

def result(request):

	total_result_list = Result.objects.filter(result_id=1)
	total_pass_percent, total_fail_percent, total_pending_percent = count_function(total_result_list)

	security_result_list = select_category(1, 1)
	security_pass_percent, security_fail_percent, security_pending_percent = count_function(security_result_list)

	clouddesign_result_list = select_category(1, 2)
	clouddesign_pass_percent, clouddesign_fail_percent, clouddesign_pending_percent = count_function(clouddesign_result_list)

	highability_result_list = select_category(1, 3)
	highability_pass_percent, highability_fail_percent, highability_pending_percent = count_function(highability_result_list)

	cloudmanage_result_list = select_category(1, 4)
	cloudmanage_pass_percent, cloudmanage_fail_percent, cloudmanage_pending_percent = count_function(cloudmanage_result_list)

	infrastructure_result_list = select_category(1, 5)
	infrastructure_pass_percent, infrastructure_fail_percent, infrastructure_pending_percent = count_function(infrastructure_result_list)


	basic_result_list = select_package(1, 1)
	basic_pass_percent, basic_fail_percent, basic_pending_percent = count_function(basic_result_list)

	professional_result_list_tmp = select_package(1, 2) | basic_result_list
	professional_result_list = sorted(professional_result_list_tmp, key=operator.attrgetter('question.q_id'))
	professional_pass_percent, professional_fail_percent, professional_pending_percent = count_function(professional_result_list)

	enterprise_result_list_tmp = select_package(1, 3) | professional_result_list_tmp | basic_result_list
	enterprise_result_list = sorted(enterprise_result_list_tmp, key=operator.attrgetter('question.q_id'))
	enterprise_pass_percent, enterprise_fail_percent, enterprise_pending_percent = count_function(enterprise_result_list)

	return render(request, 'report/report.html', locals())
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