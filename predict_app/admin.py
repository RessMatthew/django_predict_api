from django.contrib import admin

# Register your models here.
from predict_app.models import TrainingResult

admin.site.register(TrainingResult)  # 注册Man到后台