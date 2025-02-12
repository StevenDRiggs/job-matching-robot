from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'jmr2/login_page.html'
