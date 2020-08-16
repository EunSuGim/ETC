from django.contrib import admin
from polls import models
# Register your models here.


admin.site.register(models.Posts)
admin.site.register(models.Answer)