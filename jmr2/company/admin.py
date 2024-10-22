# TODO: enhance admin site by using inlines

from django.contrib import admin

from .models import *


# class PositionInline(admin.StackedInline):
#     model = Position
#     extra = 1
# 
# class TaskInline(admin.TabularInline):
#     model = Position.tasks.through
#     extra = 1
# 
# class SkillInline(admin.TabularInline):
#     model = Position.skills.through
#     extra = 1
# 
class SkillDetailInline(admin.TabularInline):
    model = SkillDetail
    extra = 1

class TraitDetailInline(admin.TabularInline):
    model = TraitDetail
    extra = 1

# class CompanyAdmin(admin.ModelAdmin):
#     inlines = [PositionInline]
# 
# class PositionAdmin(admin.ModelAdmin):
#     inlines = [TaskInline, SkillDetailInline]
# 
class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillDetailInline]

class TraitAdmin(admin.ModelAdmin):
    inlines = [TraitDetailInline]


# admin.site.register(Company, CompanyAdmin)
admin.site.register(Company)
# admin.site.register(Position, PositionAdmin)
admin.site.register(Position)
admin.site.register(Task)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Trait, TraitAdmin)
