from django.db import models

# Create your models here.
class DemoCategory(models.Model):
	# 驗測表五大面向
	# ('雲端安全設計'),
	# ('雲端架構設計'),
	# ('服務可靠度'),
	# ('雲端服務管理'),
	# ('基楚設施完備性'),
	demo_category_name = models.CharField(max_length=20)

	def __str__(self):
		return self.demo_category_name

class DemoMethod(models.Model):
	# view, testing 兩種測試方試
	demo_method_name = models.CharField(max_length=10)

	def __str__(self):
		return self.demo_method_name

class DemoStatus(models.Model):
	demo_status_name = models.CharField(max_length=10, default='pending')

	def __str__(self):
		return self.demo_status_name

class DemoStarLevel(models.Model):
	# 方案: 三星, 四星, 五星
	demo_star_level = models.CharField(max_length=10)

	def __str__(self):
		return self.demo_star_level

class DemoQuestion(models.Model):
	q_id = models.IntegerField()
	q_category = models.ForeignKey('DemoCategory', related_name='category')
	q_star = models.ForeignKey('DemoStarLevel', related_name='star_level', null=True)
	q_item = models.CharField(max_length=50)
	q_index = models.CharField(max_length=200)
	q_explanation = models.CharField(max_length=200)
	q_method = models.ForeignKey('DemoMethod', related_name='method')

	def __str__(self):
		return str(self.q_id)