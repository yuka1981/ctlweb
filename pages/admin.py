from django.contrib import admin
from .models import DemoCategory, DemoMethod, DemoStatus, DemoStarLevel, DemoQuestion

@admin.register(DemoCategory)
class DemoCategorysAdmin(admin.ModelAdmin):
    list_display = ('demo_category_name',)

@admin.register(DemoMethod)
class DemoMethodsAdmin(admin.ModelAdmin):
    list_display = ('demo_method_name',)

@admin.register(DemoStatus)
class DemoStatusAdmin(admin.ModelAdmin):
    list_display = ('demo_status_name',)

@admin.register(DemoStarLevel)
class DemoStarLevelsAdmin(admin.ModelAdmin):
    list_display = ('demo_star_level',)

@admin.register(DemoQuestion)
class DemoQuestionsAdmin(admin.ModelAdmin):
    list_display = ('q_id', 'q_category', 'q_item', 'q_index', 'q_explanation', 'q_method')
