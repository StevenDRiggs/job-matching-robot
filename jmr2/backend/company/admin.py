# TODO: enhance admin site by using inlines

from django.contrib import admin

from .models import *


admin.site.register(Benefit)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(Task)
admin.site.register(Trait)
