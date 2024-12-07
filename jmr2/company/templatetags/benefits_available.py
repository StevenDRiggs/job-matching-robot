from django import template

from company.models import BenefitAvailable


register = template.Library()


@register.simple_tag
def benefits_availability(benefit, position):
    return BenefitAvailable.objects.filter(benefit=benefit, position=position).first().available
