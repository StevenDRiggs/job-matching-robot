import json

from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from .models import (
    Address,
    CareerField,
    CareerSubfield,
    Industry,
    Preferences,
    Skill,
    SkillLevel,
    Trait,
    TraitLevel,
    User,
    WorkTask,
)


class PreferencesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {
            'widget': JSONEditorWidget,
        },
    }


admin.site.register(Address)
admin.site.register(CareerField)
admin.site.register(CareerSubfield)
admin.site.register(Industry)
admin.site.register(Preferences, PreferencesAdmin)
admin.site.register(Skill)
admin.site.register(SkillLevel)
admin.site.register(Trait)
admin.site.register(TraitLevel)
admin.site.register(User)
admin.site.register(WorkTask)
