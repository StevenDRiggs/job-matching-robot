from django.views.generic import TemplateView


class SignUpPageView(TemplateView):
    template_name = 'jmr2/signup_page.html'
