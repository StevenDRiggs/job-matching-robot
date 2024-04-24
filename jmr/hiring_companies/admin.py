from django.contrib import admin

from .models import (
    CareerField,
    CareerSubfield,
    Company,
    Industry,
    JobLocation,
    JobRequirements,
    Skill,
    SkillLevel,
    Trait,
    TraitLevel,
    WorkTask,
)


admin.site.register(CareerField)
admin.site.register(CareerSubfield)
admin.site.register(Company)
admin.site.register(Industry)
admin.site.register(JobLocation)
admin.site.register(JobRequirements)
admin.site.register(Skill)
admin.site.register(SkillLevel)
admin.site.register(Trait)
admin.site.register(TraitLevel)
admin.site.register(WorkTask)
