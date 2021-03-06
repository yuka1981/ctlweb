from django.db import models

# Create your models here.
class Project(models.Model):
	# pid = models.IntegerField(default=1)
	project_name = models.CharField(max_length=50)
	# powner = models.ForeignKey('User', related_name='username')

	def __str__(self):
		return self.project_name

class Category(models.Model):
	# 驗測表五大面向
	#	('network_app_security', '網路/應用程式安全性'),
	# 	('cloud_computing_design', '雲端運算架構設計'),
	# 	('operation_function', '運營功能完備度'),
	# 	('system_high_availability', '系統可靠度'),
	# 	('infrastructure', '基楚設施完成度'),
	category_name = models.CharField(max_length=20)

	def __str__(self):
		return self.category_name

class Method(models.Model):
	# view, testing 兩種測試方試
	method_name = models.CharField(max_length=10)

	def __str__(self):
		return self.method_name

class Status(models.Model):
	status_name = models.CharField(max_length=10, default='pending')

	def __str__(self):
		return self.status_name

class StarLevel(models.Model):
	# 方案: 三星, 四星, 五星
	star_name = models.CharField(max_length=10, default='3')

	def __str__(self):
		return self.star_name

class DataUpload(models.Model):
	file_description = models.CharField(max_length=100, blank=True, null=True)
	file_upload = models.FileField(upload_to='doc', null=True)
	file_time_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.file_name

class Question(models.Model):
	q_id = models.IntegerField()
	q_category = models.ForeignKey('Category', related_name='category')
	q_star = models.ForeignKey('StarLevel', related_name='star_level', null=True, blank=True)
	q_item = models.CharField(max_length=50)
	q_index = models.CharField(max_length=200)
	q_explanation =  models.CharField(max_length=200)
	q_method = models.ForeignKey('Method', related_name='method')

	def __str__(self):
		return str(self.q_id)

class Result(models.Model):
	result_id = models.IntegerField(default=1)
	project_name = models.ForeignKey('Project', related_name='project')
	question = models.ForeignKey('Question', related_name='result_items')
	status = models.ForeignKey('Status', related_name='status')
	evidence = models.CharField(max_length=200, blank=True)
	result_file = models.ForeignKey('DataUpload', related_name='dataupload', null=True, blank=True)

	def __str__(self):
	 	return str(self.result_id)
