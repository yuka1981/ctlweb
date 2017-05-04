from django.contrib import admin
from .models import Project, Category, Method, Status, StarLevel, Question, Result, DataUpload, WebContent

class ResultInline(admin.TabularInline):
    model = Result

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', )

@admin.register(Category)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(Method)
class MethodsAdmin(admin.ModelAdmin):
    list_display = ('method_name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)

@admin.register(StarLevel)
class StarLevelsAdmin(admin.ModelAdmin):
    list_display = ('star_name',)

@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('q_id', 'q_category', 'q_item', 'q_index', 'q_explanation', 'q_method',)
    inlines = [ResultInline]

@admin.register(Result)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'project_name', 'question', 'status', 'evidence',)

@admin.register(DataUpload)
class DataUploadsAdmin(admin.ModelAdmin):
    list_display = ('file_description', 'file_upload', 'file_time_at',)

@admin.register(WebContent)
class WebContentsAdmin(admin.ModelAdmin):
    list_display = ('web_category_name', 'web_category_content')
