import json

from django.http import JsonResponse

from .models import *


def benefits_index(req):
    benefits = json.dumps([{'pk': b.pk, 'tag': b.tag} for b in Benefit.objects.all()])

    return JsonResponse(benefits, safe=False)

def benefit_page(req, pk):
    benefit = Benefit.objects.get(pk=pk)
    benefit_json = json.dumps({
        'pk': pk,
        'tag': benefit.tag,
        'description': benefit.description,
    })

    return JsonResponse(benefit_json, safe=False)


def companies_index(req):
    companies = json.dumps([{'pk': c.pk, 'name': c.name} for c in Company.objects.all()])

    return JsonResponse(companies, safe=False)

def company_page(req, pk):
    company = Company.objects.get(pk=pk)
    company_json = json.dumps({
        'pk': pk,
        'name' : company.name,
        'positions': [{'pk': p.pk, 'title': p.title} for p in company.positions.all()],
    })

    return JsonResponse(company_json, safe=False)


def positions_index(req):
    positions = json.dumps([{'pk': p.pk, 'title': p.title} for p in Position.objects.all()])

    return JsonResponse(positions, safe=False)

def position_page(req, pk):
    position = Position.objects.get(pk=pk)
    position_json = json.dumps({
        'pk': pk,
        'title': position.title,
        'company': position.company.name,
        'description': position.description,
        'location': position.get_location(),
        'relocation_assistance': position.get_relocation_assistance(),
        'position_type': position.get_position_type(),
        'pay': position.get_pay(),
        'pay_frequency': position.get_pay_frequency(),
        'hours': position.get_hours(),
        'benefits': position.get_benefits(),
        'tasks': [{'pk': t.pk, 'tag': t.tag} for t in position.tasks.all()],
        'skills': {
            'required': position.get_required_skills(),
            'preferred': position.get_preferred_skills(),
            'bonus': position.get_bonus_skills(),
        },
        'traits': {
            'required': position.get_required_traits(),
            'preferred': position.get_preferred_traits(),
            'bonus': position.get_bonus_traits(),
        },
    })

    return JsonResponse(position_json, safe=False)


def skills_index(req):
    skills = json.dumps([{'pk': s.pk, 'tag': s.tag} for s in Skill.objects.all()])

    return JsonResponse(skills, safe=False)

def skill_page(req, pk):
    skill = Skill.objects.get(pk=pk)
    skill_json = json.dumps({'pk': pk, 'tag': skill.tag})

    return JsonResponse(skill_json, safe=False)


def tasks_index(req):
    tasks = json.dumps([{'pk': t.pk, 'tag': t.tag} for t in Task.objects.all()])

    return JsonResponse(tasks, safe=False)

def task_page(req, pk):
    task = Task.objects.get(pk=pk)
    task_json = json.dumps({
        'pk': pk,
        'tag': task.tag,
        'description': task.description,
    })

    return JsonResponse(task_json, safe=False)


def traits_index(req):
    traits = json.dumps([{'pk': t.pk, 'tag': t.tag} for t in Trait.objects.all()])

    return JsonResponse(traits, safe=False)

def trait_page(req, pk):
    trait = Trait.objects.get(pk=pk)
    trait_json = json.dumps({'pk': pk, 'tag': trait.tag})

    return JsonResponse(trait_json, safe=False)
