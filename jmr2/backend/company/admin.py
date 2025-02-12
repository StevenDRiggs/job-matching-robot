# TODO: enhance admin site by using inlines

from django.contrib import admin

from .models import *


# class PositionInline(admin.StackedInline):
#     model = Position
#     extra = 1
# 
# class BenefitInline(admin.StackedInline):
#     model = Position.benefits.through
#     extra = 1
# 
# class BenefitAvailableInline(admin.StackedInline):
#     model = BenefitAvailable
#     extra = 1
# 
# class SkillInline(admin.TabularInline):
#     model = Position.skills.through
#     extra = 1
# 
# class SkillDetailInline(admin.TabularInline):
#     model = SkillDetail
#     extra = 1
# 
# class TraitInline(admin.TabularInline):
#     model = Position.traits.through
#     extra = 1
# 
# class TraitDetailInline(admin.TabularInline):
#     model = TraitDetail
#     extra = 1
# 
# 
# class CompanyAdmin(admin.ModelAdmin):
#     inlines = [PositionInline]
# 
# class PositionAdmin(admin.ModelAdmin):
#     inlines = [BenefitAvailableInline, SkillDetailInline, TraitDetailInline]
# 
# class BenefitAdmin(admin.ModelAdmin):
#     inlines = [BenefitAvailableInline]
# 
# class SkillAdmin(admin.ModelAdmin):
#     inlines = [SkillDetailInline]
# 
# class TraitAdmin(admin.ModelAdmin):
#     inlines = [TraitDetailInline]
# 
# 
# admin.site.register(Company, CompanyAdmin)
# admin.site.register(Position, PositionAdmin)
# admin.site.register(Task)
# admin.site.register(Benefit, BenefitAdmin)
# admin.site.register(Skill, SkillAdmin)
# admin.site.register(Trait, TraitAdmin)

admin.site.register(Benefit)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(Task)
admin.site.register(Trait)
